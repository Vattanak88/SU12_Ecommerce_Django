# 🏪 EcommerceFinal - Django E-Commerce Platform with Docker

A complete Django-based e-commerce platform with shopping cart, checkout, KHQR payment integration, and Docker deployment.

## ✨ Features

- ✅ **Product Catalog** - Browse products by category
- ✅ **Shopping Cart** - Add/remove items, update quantities
- ✅ **Checkout System** - Multi-step checkout with customer information
- ✅ **Payment Processing** - KHQR (Bakong) QR code-based payments
- ✅ **Order Management** - Track orders and payment status
- ✅ **Email Notifications** - Gmail SMTP integration
- ✅ **Admin Dashboard** - Manage products, orders, customers
- ✅ **REST API** - JSON endpoints for frontend integration
- ✅ **Responsive Design** - Mobile-friendly UI with Vue.js
- ✅ **Docker Ready** - Complete Docker & Docker Compose setup

## 📊 Project Information

| Aspect | Details |
|--------|---------|
| **Framework** | Django 5.2.5 |
| **Database** | MySQL 8.0 |
| **Server** | Gunicorn + Nginx |
| **Frontend** | Vue.js + Axios |
| **Payments** | KHQR (Bakong) |
| **Email** | Gmail SMTP |
| **Deployment** | Docker & Docker Compose |
| **OS Target** | Ubuntu 24.02 LTS |

## 📦 Database Analysis

**Single Database Management System: MySQL 8.0**

### Database Tables (16 main tables)

#### Core Django Tables (7)
- `auth_user` - User authentication
- `auth_group` - User groups/roles
- `auth_permission` - Permissions
- `django_migrations` - Schema versions
- `django_sessions` - Session management
- `django_content_type` - Content framework
- `django_admin_log` - Admin activity logs

#### E-Commerce Tables (9)
- `home_category` - Product categories
- `home_product` - Product catalog
- `home_cart` - Shopping cart items
- `home_checkout` - Customer checkout info
- `home_order` - Orders
- `home_orderdetail` - Order items
- `home_payment` - Payment records
- `home_slider` - Homepage sliders
- `home_feature` - Featured products

## 📞 Communication Systems

### Email ✅ Implemented
- **Method**: Django SMTP backend
- **Provider**: Gmail or any SMTP server
- **Usage**: Contact form, order confirmations
- **Configuration**: Set in `.env` file

### Telegram ⚠️ Imported (Ready to Implement)
- **Library**: `python-telegram-bot==22.5`
- **Purpose**: Order notifications, payment alerts
- **Status**: Can be extended in views.py

### Payment Notifications
- **QR Code**: Generated for Bakong payments
- **Status API**: Check payment status via Bakong API

## 🚀 Quick Start

### Prerequisites
- Docker & Docker Compose installed
- Ubuntu 24.02 LTS (for VPS)

### Local Development

```bash
# Clone repository
git clone https://github.com/MengSonly17/Ecommerce_midterm_group2.git
cd Ecommerce_midterm_group2

# Create environment file
cp .env.example .env

# Edit environment variables
nano .env

# Build Docker images
docker-compose build

# Start services
docker-compose up -d

# Initialize database
docker-compose exec web python manage.py migrate

# Create admin user
docker-compose exec web python manage.py createsuperuser

# Access application
# Website: http://localhost:8000
# Admin: http://localhost:8000/admin
```

## 📚 Documentation

### Comprehensive Guides

1. **[PROJECT_DOCUMENTATION.md](PROJECT_DOCUMENTATION.md)**
   - Complete project overview
   - Feature list and technology stack
   - Installation instructions
   - Docker deployment theory

2. **[DOCKER_DEPLOYMENT_GUIDE.md](DOCKER_DEPLOYMENT_GUIDE.md)**
   - **FOR BEGINNERS**: Step-by-step VPS deployment
   - How to set up Ubuntu 24.02 LTS
   - Complete Docker configuration
   - Domain and SSL setup
   - Monitoring and maintenance
   - Troubleshooting guide

## 🐳 Docker Files Included

```
├── Dockerfile              # Application container blueprint
├── docker-compose.yml      # Multi-container orchestration
├── entrypoint.sh          # Container startup script
├── .env.example           # Environment variables template
├── .dockerignore          # Docker build exclusions
└── .gitignore             # Git exclusions
```

## 🔧 Docker Commands

### Start & Stop
```bash
# Start all containers
docker-compose up -d

# Stop all containers
docker-compose down

# View running containers
docker-compose ps
```

### Database Operations
```bash
# Apply migrations
docker-compose exec web python manage.py migrate

# Create admin user
docker-compose exec web python manage.py createsuperuser

# Backup database
docker-compose exec db mysqldump -u ecommerce_user -p ecommerceforfinal > backup.sql

# Restore database
docker-compose exec db mysql -u ecommerce_user -p ecommerceforfinal < backup.sql
```

### Logs & Monitoring
```bash
# View all logs
docker-compose logs -f

# View web app logs
docker-compose logs -f web

# View database logs
docker-compose logs -f db

# Check resource usage
docker stats
```

### Maintenance
```bash
# Restart services
docker-compose restart

# Collect static files
docker-compose exec web python manage.py collectstatic --noinput

# Enter container shell
docker-compose exec web bash

# Run Django management commands
docker-compose exec web python manage.py <command>
```

## 📝 Configuration

### Environment Variables (.env)

```env
# Django
DEBUG=False
SECRET_KEY=your-secret-key-here
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1,yourdomain.com

# Database
DB_ENGINE=django.db.backends.mysql
DB_NAME=ecommerceforfinal
DB_USER=ecommerce_user
DB_PASSWORD=your_password
DB_HOST=db
DB_PORT=3306

# Email
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

### Email Configuration (Gmail)

1. Enable 2-Factor Authentication on Gmail
2. Generate App Password at https://myaccount.google.com/apppasswords
3. Add to `.env`:
   ```env
   EMAIL_HOST_USER=your-email@gmail.com
   EMAIL_HOST_PASSWORD=xxxx xxxx xxxx xxxx
   ```

## 📊 Project Structure

```
EcommerceFinal/
├── manage.py                 # Django CLI
├── requirements.txt          # Python dependencies
├── db.sql                    # Database dump
│
├── EcommerceFinal/           # Project settings
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── Home/                     # Main app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── migrations/
│   └── static/
│
├── Core/                     # Utilities app
│   ├── models.py
│   ├── views.py
│   └── management/commands/
│
├── templates/               # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── shop.html
│   ├── cart.html
│   ├── checkout.html
│   ├── payment.html
│   └── contact.html
│
├── media/                   # User-uploaded files
│   └── qrcodes/
│
├── Dockerfile
├── docker-compose.yml
├── entrypoint.sh
├── .env.example
├── .gitignore
├── .dockerignore
├── PROJECT_DOCUMENTATION.md
└── DOCKER_DEPLOYMENT_GUIDE.md
```

## 🚀 Deployment (VPS)

**See [DOCKER_DEPLOYMENT_GUIDE.md](DOCKER_DEPLOYMENT_GUIDE.md) for complete step-by-step instructions.**

### Quick Summary
1. Update system: `apt-get update && apt-get upgrade -y`
2. Install Docker: `apt-get install -y docker.io docker-compose`
3. Clone project: `git clone <repo-url> && cd <project>`
4. Configure: `cp .env.example .env && nano .env`
5. Deploy: `docker-compose build && docker-compose up -d`
6. Initialize: `docker-compose exec web python manage.py migrate`
7. Create admin: `docker-compose exec web python manage.py createsuperuser`
8. Setup Nginx & SSL (see full guide)

## ⚙️ System Requirements

### Local Development
- Docker & Docker Compose
- 4GB RAM minimum
- 5GB disk space

### VPS Requirements (Ubuntu 24.02 LTS)
- 2GB RAM minimum (4GB recommended)
- 20GB disk space minimum (50GB recommended)
- Docker & Docker Compose installed
- Root or sudo access

## 🔐 Security

- ✅ Environment variables for secrets (not in code)
- ✅ DEBUG=False in production
- ✅ Strong SECRET_KEY
- ✅ CSRF protection enabled
- ✅ SSL/TLS support (Let's Encrypt)
- ✅ Database credentials in environment
- ✅ Git ignores sensitive files

## 🐛 Troubleshooting

### Database won't connect
```bash
docker-compose logs db
docker-compose restart db
```

### Static files not loading
```bash
docker-compose exec web python manage.py collectstatic --noinput
docker-compose restart web
```

### Email not sending
```bash
# Verify .env EMAIL settings
# Check Gmail "App passwords" configuration
# Test with: docker-compose exec web python manage.py shell
# >>> from django.core.mail import send_mail
# >>> send_mail("Test", "Message", "from@gmail.com", ["to@gmail.com"])
```

### Container won't start
```bash
docker-compose logs web
docker-compose build --no-cache
docker-compose up -d
```

See [DOCKER_DEPLOYMENT_GUIDE.md](DOCKER_DEPLOYMENT_GUIDE.md) for more troubleshooting.

## 📞 Support

- **Django**: https://docs.djangoproject.com/
- **Docker**: https://docs.docker.com/
- **MySQL**: https://dev.mysql.com/doc/

## 📋 Technology Stack

- **Backend**: Django 5.2.5, Django REST Framework 3.16.1
- **Database**: MySQL 8.0, mysqlclient 2.2.7
- **Server**: Gunicorn 23.0.0, Nginx
- **Frontend**: Vue.js, Axios, Bootstrap
- **Containerization**: Docker, Docker Compose
- **Payment**: KHQR (Bakong)
- **Email**: Gmail SMTP
- **Messaging**: Python Telegram Bot (ready to use)

## 📄 License

This project is for educational purposes.

## 👥 Contributors

- Group 2 - Setec University
- MengSonly17

## 🎓 Learning Outcomes

After completing this project, you'll have learned:
- Django web development
- MySQL database design
- Docker containerization
- Linux/VPS administration
- Payment gateway integration
- Email configuration
- REST API development
- Production deployment

## 🎯 Next Steps

1. ✅ Read [PROJECT_DOCUMENTATION.md](PROJECT_DOCUMENTATION.md) for overview
2. ✅ Read [DOCKER_DEPLOYMENT_GUIDE.md](DOCKER_DEPLOYMENT_GUIDE.md) for deployment
3. ✅ Configure `.env` file
4. ✅ Deploy using Docker
5. ✅ Add products via admin panel
6. ✅ Test checkout and payments
7. ✅ Monitor logs and performance
8. ✅ Setup automated backups

---

**Ready to deploy? Start with [DOCKER_DEPLOYMENT_GUIDE.md](DOCKER_DEPLOYMENT_GUIDE.md)** 🚀
