# VPS Quick Reference - Command Cheat Sheet

## SSH & Connection

```bash
# Connect to VPS
ssh root@your-vps-ip
ssh root@your-domain.com

# Exit VPS
exit

# Copy files to VPS
scp file.txt root@your-vps-ip:/home/
scp -r folder root@your-vps-ip:/home/
```

## System Management

```bash
# Update system
apt-get update
apt-get upgrade -y

# Check disk space
df -h

# Check memory usage
free -h

# View running processes
ps aux | grep docker

# Check system logs
journalctl -n 50 -f
```

## Docker Commands

### Container Management
```bash
# Start services
cd /home/ecommerce
docker-compose up -d

# Stop services
docker-compose down

# Restart all
docker-compose restart

# Restart specific service
docker-compose restart web
docker-compose restart db

# View status
docker-compose ps

# View logs (all)
docker-compose logs

# Follow logs real-time
docker-compose logs -f web      # Web app logs
docker-compose logs -f db       # Database logs

# Enter container
docker-compose exec web bash
docker-compose exec db bash

# Remove everything (WARNING - loses data)
docker-compose down -v
```

### Build & Deploy
```bash
# Build images
docker-compose build

# Rebuild without cache
docker-compose build --no-cache

# Pull latest code
git pull origin main

# Build new version
docker-compose build

# Deploy new version
docker-compose up -d

# Apply migrations after update
docker-compose exec web python manage.py migrate
```

## Django Management

```bash
# Apply migrations
docker-compose exec web python manage.py migrate

# Create superuser
docker-compose exec web python manage.py createsuperuser

# Collect static files
docker-compose exec web python manage.py collectstatic --noinput

# Create cache table
docker-compose exec web python manage.py createcachetable

# Run Django shell
docker-compose exec web python manage.py shell

# Make migrations
docker-compose exec web python manage.py makemigrations

# Load initial data
docker-compose exec web python manage.py loaddata initial_data.json
```

## Database Operations

```bash
# Access MySQL
docker-compose exec db mysql -u ecommerce_user -p ecommerceforfinal

# MySQL commands (once inside mysql)
SHOW DATABASES;
USE ecommerceforfinal;
SHOW TABLES;
SELECT * FROM home_product LIMIT 5;
EXIT;

# Backup database
docker-compose exec db mysqldump -u ecommerce_user -p ecommerceforfinal > backup.sql

# Backup with date
docker-compose exec db mysqldump -u ecommerce_user -p ecommerceforfinal > backup_$(date +%Y%m%d).sql

# Restore database
docker-compose exec db mysql -u ecommerce_user -p ecommerceforfinal < backup.sql

# Check database size
docker-compose exec db mysql -u ecommerce_user -p -e "SELECT table_schema 'Database', SUM(data_length + index_length) / 1024 / 1024 'Size in MB' FROM information_schema.tables GROUP BY table_schema;"
```

## File & Folder Management

```bash
# List files
ls -la

# Change directory
cd /home/ecommerce

# Create directory
mkdir new_folder

# Remove file
rm filename.txt

# Remove folder
rm -rf folder_name

# Copy file
cp source.txt destination.txt

# Copy folder
cp -r source_folder destination_folder

# Move/rename
mv old_name.txt new_name.txt

# View file
cat filename.txt
nano filename.txt  # Edit file

# Search in files
grep "search_term" filename.txt

# Find files
find . -name "*.py"
```

## Nginx Management

```bash
# Test nginx configuration
nginx -t

# Start nginx
systemctl start nginx

# Stop nginx
systemctl stop nginx

# Restart nginx
systemctl restart nginx

# Reload nginx (without stopping)
systemctl reload nginx

# Enable auto-start
systemctl enable nginx

# View nginx logs
tail -f /var/log/nginx/access.log
tail -f /var/log/nginx/error.log
```

## SSL Certificate (Let's Encrypt)

```bash
# Install certbot
apt-get install -y certbot python3-certbot-nginx

# Get certificate
certbot --nginx -d your-domain.com -d www.your-domain.com

# Renew certificate (runs automatically)
certbot renew

# Test renewal
certbot renew --dry-run

# View certificates
certbot certificates

# Delete certificate
certbot delete --cert-name your-domain.com
```

## Monitoring & Health Checks

```bash
# View resource usage
docker stats

# Check if containers are healthy
docker-compose ps

# View container health
docker inspect ecommerce_db | grep -A 10 Health

# Check web app is responding
curl http://localhost:8000

# Check database
docker-compose exec db mysqladmin -u ecommerce_user -p ping

# View system uptime
uptime

# Check active connections
netstat -tulpn | grep LISTEN

# View port 8000
netstat -tulpn | grep 8000
```

## Deployment Workflow

```bash
# 1. SSH to VPS
ssh root@your-vps-ip

# 2. Go to project
cd /home/ecommerce

# 3. Pull latest code
git pull origin main

# 4. Build images
docker-compose build

# 5. Start services
docker-compose up -d

# 6. Run migrations
docker-compose exec web python manage.py migrate

# 7. Collect static files
docker-compose exec web python manage.py collectstatic --noinput

# 8. Check status
docker-compose ps

# 9. Check logs
docker-compose logs -f web

# 10. Test website
curl http://localhost:8000
```

## Backup & Restore

### Full Backup
```bash
# Create backup directory
mkdir ~/backups
cd ~/backups

# Backup database
docker-compose exec db mysqldump -u ecommerce_user -p ecommerceforfinal > db_backup.sql

# Backup media files
tar -czf media_backup.tar.gz /home/ecommerce/media/

# Backup project files (if needed)
tar -czf project_backup.tar.gz /home/ecommerce/

# List backups
ls -lh
```

### Restore Backup
```bash
# Restore database
docker-compose exec db mysql -u ecommerce_user -p ecommerceforfinal < db_backup.sql

# Restore media files
tar -xzf media_backup.tar.gz -C /home/ecommerce/
```

## Troubleshooting

### Check Logs
```bash
# Docker logs
docker-compose logs web

# System logs
journalctl -n 100 -f

# Nginx errors
tail -f /var/log/nginx/error.log

# Django logs
docker-compose logs -f web | grep ERROR
```

### Restart Everything
```bash
cd /home/ecommerce
docker-compose down
docker-compose up -d
docker-compose logs -f web
```

### Fix Permission Issues
```bash
# Give ownership
chown -R ubuntu:ubuntu /home/ecommerce

# Make script executable
chmod +x entrypoint.sh
chmod +x script.sh
```

### Clean Up Docker
```bash
# Remove unused containers
docker container prune -f

# Remove unused images
docker image prune -a -f

# Remove unused volumes
docker volume prune -f

# Full cleanup
docker system prune -a -f
```

## Performance Optimization

```bash
# Check slow queries
docker-compose exec db mysql -u ecommerce_user -p -e "SHOW PROCESSLIST;"

# View memory usage
docker stats ecommerce_web

# Increase workers (edit docker-compose.yml)
# Change: --workers 4 to --workers 8

# Check cache hit rate
docker-compose exec web python manage.py shell
>>> from django.core.cache import cache
>>> cache.get('test_key')

# Monitor network
watch -n 1 'docker stats'
```

## Important File Locations

```bash
# Project root
/home/ecommerce

# Environment file
/home/ecommerce/.env

# Docker compose file
/home/ecommerce/docker-compose.yml

# Nginx config
/etc/nginx/sites-available/ecommerce

# SSL certificates
/etc/letsencrypt/live/your-domain.com

# Media files
/home/ecommerce/media

# Static files
/home/ecommerce/Home/static

# Logs
/var/log/nginx/

# Docker volumes
/var/lib/docker/volumes/
```

## Safety Tips

✅ **Always backup before major changes:**
```bash
docker-compose exec db mysqldump -u ecommerce_user -p ecommerceforfinal > backup.sql
```

✅ **Test on development first:**
- Don't change .env directly
- Test in docker-compose first
- Use dry-run before actual changes

✅ **Monitor after changes:**
```bash
docker-compose logs -f web
```

✅ **Keep backups off-site:**
```bash
# Download backup to local machine
scp root@your-vps-ip:/home/ecommerce/backup.sql ~/backups/
```

✅ **Regular maintenance:**
```bash
# Monthly: Check disk space
df -h

# Monthly: Update system
apt-get update && apt-get upgrade -y

# Weekly: Backup database
docker-compose exec db mysqldump -u ecommerce_user -p ecommerceforfinal > backup.sql

# Daily: Check logs
docker-compose logs | grep ERROR
```

## Common Issues & Solutions

### Port Already in Use
```bash
# Find process using port 8000
lsof -i :8000

# Kill process
kill -9 <PID>

# Or change port in docker-compose.yml
# From: "8000:8000"
# To: "8001:8000"
```

### Database Connection Failed
```bash
docker-compose logs db
docker-compose restart db
sleep 15
docker-compose restart web
```

### Out of Disk Space
```bash
df -h
docker image prune -a -f
docker volume prune -f
docker system prune -a -f
```

### Container Keeps Restarting
```bash
docker-compose logs web
docker-compose build --no-cache
docker-compose up -d
```

---

**Save this file for quick reference: `commands.md`** 📋
