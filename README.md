# MySQL Database Backup & Recovery Techniques

This project demonstrates and evaluates various database backup and recovery methods using MySQL.  
It benchmarks multiple techniques based on performance metrics such as backup duration, restore time, CPU usage, memory usage, disk I/O, and backup file size.  
The goal is to identify the most effective strategies for different operational scenarios.

---

## 📌 Project Overview
The project involves creating a test database (`test_db`) with synthetic employee data and applying different backup and recovery methods.  
Performance results are recorded and analyzed to compare the efficiency, scalability, and practicality of each technique.

---

## 🔹 Backup & Recovery Techniques Tested
1. **Full Backup** – Complete `.sql` export using `mysqldump`.
2. **Incremental Backup** – Captures only changes since last backup using MySQL binary logs.
3. **Differential Backup** – Captures changes since the last full backup.
4. **Point-in-Time Recovery (PITR)** – Restores database to a specific timestamp using binary logs.
5. **Transaction Log Restoration** – Uses binary logs to recover specific transactions.
6. **Cloud-Based Backup** – Uploads backups to cloud storage (e.g., OneDrive, Google Drive, S3).
7. **Hot Backup** – Backup while database is online (e.g., Percona XtraBackup).
8. **Cold Backup** – Backup while database is offline via file copy.

---

## ⚙️ Experimental Setup
- **Database:** MySQL Server 8.0
- **OS:** Windows 11
- **Hardware:** Intel Processor, 16 GB RAM, SSD storage
- **Tools Used:**
  - `mysqldump` & `mysql` CLI
  - `mysqlbinlog` for binlog operations
  - PowerShell scripts for timing backups/restores
  - Cloud sync tools for cloud backups
  - MATLAB/Python for data visualization

---

## 📂 Folder Structure
