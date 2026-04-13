# 🏥 CarePulse — Patient Management System

> A full-stack healthcare patient management application built with Next.js 14, enabling patients to register, book appointments, and receive SMS notifications — with a dedicated admin dashboard for appointment management.

🔗 **Live Demo:** [patient-management-system-ashy.vercel.app](https://patient-management-system-ashy.vercel.app)

---

## 📌 Overview

CarePulse is a modern, production-grade patient management system designed to simplify healthcare workflows. Patients can register with their medical details, schedule appointments with doctors, and get real-time SMS confirmations. Admins can view, confirm, and cancel appointments from a central dashboard — all with error monitoring baked in via Sentry.

---

## ✨ Features

- **Patient Registration** — Full onboarding form with personal info, medical history, insurance details, and document upload (ID proof)
- **Appointment Booking** — Patients can schedule appointments with their preferred doctor and reason
- **Admin Dashboard** — Secure admin panel to view all appointments, confirm or cancel them with a reason
- **SMS Notifications** — Automated SMS sent to patients on appointment confirmation via Twilio
- **Form Validation** — Robust client-side validation using React Hook Form + Zod schemas
- **Error Monitoring** — Integrated Sentry across client, server, and edge for production observability
- **Responsive UI** — Clean, accessible dark-themed interface built with Radix UI + Tailwind CSS

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Framework | Next.js 14 (App Router) |
| Language | TypeScript |
| Backend / Database | Appwrite (auth, database, storage) |
| SMS | Twilio |
| Forms | React Hook Form + Zod |
| UI Components | Radix UI + shadcn/ui |
| Styling | Tailwind CSS |
| Data Tables | TanStack Table |
| Error Monitoring | Sentry |
| Deployment | Vercel |

---

## 📂 Project Structure

```
Patient-Management-System/
│
├── app/                    # Next.js App Router pages
│   ├── page.tsx            # Patient registration / home
│   ├── patients/           # Patient-specific routes
│   └── admin/              # Admin dashboard
│
├── components/             # Reusable UI components
│   ├── forms/              # Registration & appointment forms
│   ├── table/              # Appointment data table
│   └── ui/                 # shadcn base components
│
├── lib/                    # Utility functions & Appwrite client
│   ├── actions/            # Server actions (patient, appointment)
│   └── appwrite.ts         # Appwrite SDK config
│
├── types/                  # TypeScript type definitions
├── constants/              # App-wide constants (doctors list, etc.)
├── public/                 # Static assets
│
├── sentry.client.config.ts
├── sentry.server.config.ts
├── sentry.edge.config.ts
├── next.config.mjs
├── tailwind.config.ts
└── tsconfig.json
```

---

## 🚀 Getting Started

### Prerequisites

- Node.js 18+
- An [Appwrite](https://appwrite.io) account (cloud or self-hosted)
- A [Twilio](https://twilio.com) account for SMS
- A [Sentry](https://sentry.io) project (optional, for error monitoring)

### 1. Clone the repository

```bash
git clone https://github.com/DhritiSoni4/Patient-Management-System.git
cd Patient-Management-System
```

### 2. Install dependencies

```bash
npm install
```

### 3. Set up environment variables

Create a `.env.local` file in the root directory:

```env
# Appwrite
NEXT_PUBLIC_ENDPOINT=https://cloud.appwrite.io/v1
PROJECT_ID=your_appwrite_project_id
API_KEY=your_appwrite_api_key
DATABASE_ID=your_database_id
PATIENT_COLLECTION_ID=your_patient_collection_id
APPOINTMENT_COLLECTION_ID=your_appointment_collection_id
NEXT_PUBLIC_BUCKET_ID=your_storage_bucket_id

# Admin
NEXT_PUBLIC_ADMIN_PASSKEY=your_admin_passkey

# Twilio
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE_NUMBER=your_twilio_phone_number

# Sentry (optional)
SENTRY_DSN=your_sentry_dsn
```

### 4. Run the development server

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

---

## 🔐 Admin Access

The admin dashboard is protected by a passkey. To access it:

1. Navigate to `/admin`
2. Enter the passkey set in `NEXT_PUBLIC_ADMIN_PASSKEY`

From the dashboard you can view all appointments, confirm them (which triggers an SMS to the patient), or cancel with a reason.

---

## 📋 App Workflow

```
Patient visits homepage
       ↓
Registers with personal + medical info
       ↓
Books an appointment (doctor, date, reason)
       ↓
Admin reviews in dashboard
       ↓
Admin confirms / cancels
       ↓
Patient receives SMS notification via Twilio
```

---

## 🧪 Testing

The repo includes Python-based test scripts (`test1.py` – `test4.py`) for backend validation.

```bash
python test1.py
```

---

## 📦 Key Dependencies

| Package | Purpose |
|---|---|
| `node-appwrite` | Server-side Appwrite SDK |
| `twilio` | SMS notifications |
| `@sentry/nextjs` | Error monitoring |
| `react-hook-form` | Form state management |
| `zod` | Schema validation |
| `@tanstack/react-table` | Appointment data table |
| `react-dropzone` | Document/ID upload |
| `react-phone-number-input` | International phone input |
| `react-datepicker` | Appointment date picker |

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

---

## 👤 Author

**Dhriti Soni** · [GitHub](https://github.com/DhritiSoni4)
