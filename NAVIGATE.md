# 🧭 Complete Project Navigation Guide

Welcome to the Zero-Trust Banking System! This guide is designed to walk you through exactly **how to navigate every feature** of the platform step-by-step.

The system relies on three distinct user roles, each with its own dashboard and feature set. Below is the complete roadmap.

---

## 🔗 Quick Links & Setup
*   **Frontend Application:** [http://localhost:5174](http://localhost:5174)
*   **Backend API:** [http://localhost:8000](http://localhost:8000)

*(Ensure both servers are running before starting!)*

---

## 👤 1. Regular User Navigation (Banking Features)

This is the primary flow for normal banking customers.

### Account Creation & Login
1. Open [http://localhost:5174](http://localhost:5174) in your browser.
2. Click **"Register"** or go to `http://localhost:5174/register`.
3. Fill out the form. Behind the scenes, the system will automatically generate your **RSA and ECC cryptographic keys**.
4. You will be automatically logged in and redirected to the **User Dashboard**.
   * *Alternatively*, click **"Sign In"** from the home page using an existing account.

### The Dashboard
When logged in, your main URL is `/dashboard`. Here you will see:
*   Your current **Available Balance** (initially $0.00).
*   Quick Action Buttons: **Deposit** (Green), **Send Money** (White), and **History** (Transparent).
*   A quick glance at your **Recent Transactions** below.

### Feature: How to Deposit Funds (Fake Payment Gateway)
1. On your Dashboard, click the green **Deposit** button.
2. You are now on the Deposit flow (`/deposit`).
3. **Step 1:** Enter the amount you want to deposit (e.g., `500`). Click "Continue to Payment".
4. **Step 2 (Payment Gateway):** 
   * To simulate a **SUCCESSFUL** card payment, type: `4111-1111-1111-1111`
   * To simulate a **FAILED** card payment, type: `4444-4444-4444-4444`
   * Enter any Expiry (e.g., `12/25`) and any CVV (e.g., `123`).
5. Click **"Complete Payment"**.
6. **Step 3 (Success):** The system processes the payment atomically, uses RSA to encrypt the payload, and displays a success screen. Click **"Return to Dashboard"** to see your updated balance.

### Feature: How to Send Money
1. From your Dashboard, click the white **Send Money** button.
2. You are now on the Transfer page (`/send-money`).
3. **Select Recipient:** Choose another user from the dropdown menu.
4. **Amount:** Enter the dollar amount you wish to transfer.
5. **Select Privacy Level (Crucial Feature):**
   * **Standard:** Basic transaction metadata is visible.
   * **Private Metadata:** Recipient details are partially encrypted.
   * **High Privacy:** Utilizes ECC (Elliptic Curve Cryptography) to completely encrypt the transaction payload.
6. Click **Confirm Transfer**. The backend verifies your balance, signs the transaction with HMAC-SHA256, and links it via a SHA256 Hash Chain.

### Feature: How to View Transaction History
1. From your Dashboard, click the **History** button.
2. You are now on the History page (`/history`).
3. Here you can filter by **All**, **Sent**, or **Received** transactions.
4. When you load this page, the backend automatically uses your private keys to decrypt the transaction data so you can read it.

---

## 🛡️ 2. Admin Navigation (System Monitoring)

The Admin is responsible for overseeing the entire system and suspending malicious users.

### Logging In
1. Go to [http://localhost:5174/login](http://localhost:5174/login)
2. Enter the Admin Credentials:
   * **Email:** `admin@example.com`
   * **Password:** `Admin@12345`
3. Upon logging in, the system detects your role and automatically redirects you to the **Admin Dashboard** (`/admin-dashboard`).

### Feature: User Management
1. Inside the Admin Dashboard, you will see a list of all users.
2. **Note the Encryption:** Because of the zero-trust architecture, you will notice that User Emails and Usernames appear as raw encrypted text (e.g., `eyJhbGci...`). *The admin cannot read private user details.*
3. **Suspend/Activate:** You can click the toggle buttons next to any user account to instantly Suspend them or Activate them if they are compromised.

### Feature: Global Transaction Monitoring
1. Scroll down to the **System Transactions** view.
2. You will see every single transaction flowing through the bank.
3. Similar to user details, the **Amount and Metadata are encrypted**. The admin can verify the HMAC signature and Hash Chain are valid, but they cannot spy on the financial amounts.

---

## 🏛️ 3. Authority Navigation (KYC & Key Issuance)

The Central Authority handles compliance, Know Your Customer (KYC) verification, and issuing cryptographic keys.

### Logging In
1. Go to [http://localhost:5174/login](http://localhost:5174/login)
2. Enter the Authority Credentials:
   * **Email:** `authority@example.com`
   * **Password:** `Authority@12345`
3. Upon logging in, the system detects your role and redirects you to the **Authority Dashboard** (`/authority-dashboard`).

### Feature: KYC Verification
1. On the Authority Dashboard, you will see a queue of **Pending KYC Requests** (representing users who just registered).
2. As the Authority, you act as the verification layer. Click **Approve** or **Reject** on these accounts.
3. Once **Approved**, the backend officially issues their Cryptographic Keys to their account allowing them to operate securely. 

---

## 🔒 4. Future Features to Navigate (If Implemented)

Based on the project roadmap, you may soon navigate to these areas:
*   **Profile Page (`/profile`):** To view your encrypted contact info and enable Two-Factor Authentication (2FA) via QR Code.
*   **Community Feed (`/posts`):** To write completely encrypted messages that only authorized users can decrypt.
*   **Teacher/Demo Toggle:** A switch located on pages that lets you toggle between "Readable Text" and "Raw Ciphertext" to prove the encryption works live during a presentation. 

---
