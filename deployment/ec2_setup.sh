#!/bin/bash
# ═══════════════════════════════════════════════════════════
# EC2 Ubuntu 22.04 Deployment Script — AI Resume Generator
# ═══════════════════════════════════════════════════════════
# Run: chmod +x ec2_setup.sh && sudo ./ec2_setup.sh

set -e

echo "═══════════════════════════════════════════"
echo "  AI Resume Generator — EC2 Setup"
echo "═══════════════════════════════════════════"

# ── 1. System Updates ─────────────────────────
echo "[1/7] Updating system..."
apt update && apt upgrade -y

# ── 2. Install Python 3.11 ────────────────────
echo "[2/7] Installing Python 3.11..."
apt install -y software-properties-common
add-apt-repository -y ppa:deadsnakes/ppa
apt update
apt install -y python3.11 python3.11-venv python3.11-dev python3-pip

# ── 3. Install Node.js 20 ─────────────────────
echo "[3/7] Installing Node.js 20..."
curl -fsSL https://deb.nodesource.com/setup_20.x | bash -
apt install -y nodejs

# ── 4. Install Nginx ──────────────────────────
echo "[4/7] Installing Nginx..."
apt install -y nginx

# ── 5. Setup Project ──────────────────────────
echo "[5/7] Setting up project..."
PROJECT_DIR="/home/ubuntu/resume-generator"

if [ ! -d "$PROJECT_DIR" ]; then
    echo "ERROR: Project directory not found at $PROJECT_DIR"
    echo "Upload project files first, then run this script."
    exit 1
fi

cd $PROJECT_DIR

# Python virtual environment
python3.11 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# Frontend build
cd frontend
npm install
npm run build
cd ..

# ── 6. Create .env if missing ─────────────────
if [ ! -f ".env" ]; then
    echo "[!] No .env file found. Copying from .env.example..."
    cp .env.example .env
    echo "[!] IMPORTANT: Edit .env and add your API keys:"
    echo "    nano $PROJECT_DIR/.env"
fi

# ── 7. Configure Nginx ────────────────────────
echo "[6/7] Configuring Nginx..."
cat > /etc/nginx/sites-available/resume-generator << 'NGINX'
server {
    listen 80;
    server_name _;

    # Frontend (built React files)
    root /home/ubuntu/resume-generator/frontend/dist;
    index index.html;

    # API proxy to FastAPI backend
    location /api/ {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_read_timeout 120s;
        proxy_connect_timeout 120s;
        proxy_send_timeout 120s;
    }

    # Frontend SPA fallback
    location / {
        try_files $uri $uri/ /index.html;
    }
}
NGINX

ln -sf /etc/nginx/sites-available/resume-generator /etc/nginx/sites-enabled/
rm -f /etc/nginx/sites-enabled/default
nginx -t && systemctl restart nginx

# ── 7. Create systemd service ─────────────────
echo "[7/7] Creating systemd service..."
cat > /etc/systemd/system/resume-generator.service << SERVICE
[Unit]
Description=AI Resume Generator Backend
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu/resume-generator
ExecStart=/home/ubuntu/resume-generator/venv/bin/python -m uvicorn backend.main:app --host 127.0.0.1 --port 8000
EnvironmentFile=/home/ubuntu/resume-generator/.env
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
SERVICE

systemctl daemon-reload
systemctl enable resume-generator
systemctl start resume-generator

echo ""
echo "═══════════════════════════════════════════"
echo "  DEPLOYMENT COMPLETE"
echo "═══════════════════════════════════════════"
echo ""
echo "  1. Edit your API keys:  nano $PROJECT_DIR/.env"
echo "  2. Restart backend:     sudo systemctl restart resume-generator"
echo "  3. Check status:        sudo systemctl status resume-generator"
echo "  4. View logs:           sudo journalctl -u resume-generator -f"
echo "  5. Open in browser:     http://YOUR_EC2_PUBLIC_IP"
echo ""
