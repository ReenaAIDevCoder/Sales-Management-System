# Sales Management System

A web-based Sales Management System built using Flask, Python, SQLAlchemy, HTML, CSS, JavaScript, and SQLite.

The system is designed to help organizations manage customers, leads, sales opportunities, activities, sales targets, marketing campaigns, products, accounts, and executive-level analytics from a centralized platform.

---

## 📌 Project Overview

The Sales Management System provides a centralized platform for managing the complete sales lifecycle.

It allows users to:

- Manage customers
- Manage sales leads
- Track opportunities
- Record sales activities
- Monitor sales targets
- Manage sales pipeline
- Manage accounts and renewals
- Manage marketing campaigns
- Manage products and product feedback
- Track feature requests
- View executive analytics
- Monitor regional KPIs
- Analyze win/loss performance
- View revenue forecasts

The application also provides authentication features including:

- Login
- User registration
- Password hashing
- Forgot password
- Reset password
- Logout
- Role-based access structure

---

# 🎯 Objectives

The main objectives of this project are:

1. Centralize sales-related information.
2. Improve customer and lead management.
3. Track sales opportunities throughout the sales cycle.
4. Monitor sales targets and performance.
5. Provide sales pipeline visibility.
6. Support marketing and product management.
7. Provide management-level analytics.
8. Reduce manual sales tracking.
9. Provide a structured database for sales information.
10. Provide a user-friendly web interface.

---

# 🚀 Key Features

## 🔐 Authentication

The system provides a complete authentication module.

Features include:

- User Login
- Create New Account
- Forgot Password
- Reset Password
- Logout
- Password Hashing
- Active/Inactive User Status

Passwords are stored using secure password hashing rather than plain text.

---

# 👥 Customer Management

The customer module allows users to:

- View customers
- Add new customers
- Edit customer information
- View customer details
- Store company information
- Store contact information
- Track industry
- Track customer status
- Assign customers to users

Customer information includes:

- Name
- Company
- Email
- Phone
- Address
- City
- State
- Country
- Industry
- Status
- Assigned User

---

# 🎯 Lead Management

The lead management module supports:

- Lead listing
- Lead creation
- Lead editing
- Lead details
- Lead source tracking
- Lead priority
- Lead status
- Estimated lead value

Example lead statuses include:

- New
- Qualified
- Converted
- Lost

---

# 💼 Opportunity Management

The opportunity module helps sales teams track potential deals.

Features include:

- Create opportunity
- Edit opportunity
- View opportunity details
- Track deal value
- Track probability
- Track opportunity stage
- Track expected closing date
- Track opportunity status
- Add notes

Opportunity stages can include:

- Prospecting
- Qualification
- Proposal
- Negotiation
- Closed Won
- Closed Lost

---

# 📅 Activity Management

Sales activities can be recorded and tracked.

Supported activities include:

- Calls
- Meetings
- Follow-ups
- Emails
- Other sales activities

Activity information includes:

- User
- Customer
- Opportunity
- Activity type
- Subject
- Description
- Activity date
- Duration
- Status

---

# 📊 Sales Management

The sales module provides:

- Sales targets
- Sales performance
- Sales pipeline

Sales targets include:

- Target period
- Target amount
- Achieved amount
- Start date
- End date
- Achievement percentage

---

# 👨‍💼 Manager Module

The manager module provides features for:

- Team management
- Territory management
- Discount requests
- Sales forecasting

Managers can use these features to monitor sales team performance and regional operations.

---

# 🏢 Account Management

The account management module includes:

- Customer history
- Customer satisfaction
- Account plans
- Renewals

This helps organizations maintain long-term customer relationships.

---

# 📢 Marketing Module

The marketing module supports:

- Campaign management
- Qualified leads
- Customer segmentation
- Sales and marketing collaboration

Campaign metrics can include:

- Leads generated
- Qualified leads
- Conversions
- Revenue generated
- Campaign budget
- Campaign status

---

# 📦 Product Management

The product module provides:

- Product management
- Product roadmap
- Product feedback
- Product documentation
- Feature requests

Product information can include:

- Product name
- Product code
- Description
- Category
- Price
- Version
- Roadmap status

---

# 📈 Executive Analytics

The executive module provides management-level information including:

- Analytics
- Regional KPIs
- Win/Loss analysis
- Revenue forecasting

These modules help decision-makers understand overall sales performance.

---

# 🏗️ System Architecture

The project follows a modular Flask architecture.

```text
User
  |
  v
Web Browser
  |
  v
Flask Application
  |
  +----------------------+
  |                      |
  v                      v
Routes                 Templates
  |                      |
  v                      v
Models                HTML/CSS/JS
  |
  v
SQLAlchemy
  |
  v
Database
