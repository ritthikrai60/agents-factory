# วิธีเตรียมความพร้อมสำหรับโปรเจกต์ (How to Prepare a Project)

## สิ่งที่ต้องเตรียมพร้อม (Pre-requisites)
- ติดตั้งระบบ Antigravity 2.0 ให้เรียบร้อย
- สร้างและ Initialize Repository เป้าหมายไว้แล้ว (หรือจะเป็นโปรเจกต์ใหม่ที่สร้างในโฟลเดอร์เปล่าก็ได้)

## ขั้นตอนการเตรียมโปรเจกต์ (Preparation Steps)

1. **เริ่มต้นใช้งาน Factory (Initialize the Factory Run)**
   สั่งการ Antigravity ใน Workspace ของโปรเจกต์เป้าหมายว่า:
   > "ฉันต้องการ initialize โปรเจกต์นี้ด้วย Agents Factory" (I need to initialize this project using the Agents Factory)

2. **ตอบคำถามเพื่อวิเคราะห์โปรเจกต์ (Complete the Intake)**
   Agent จะเรียกใช้งาน skill ที่ชื่อว่า `factory-prepare` และเริ่มสอบถามข้อมูลตาม checklist ในไฟล์ `templates/project-intake.md` โดยอาจจะมีคำถามเกี่ยวกับ:
   - ข้อกำหนดด้านความปลอดภัย (Security constraints)
   - ขนาดของระบบที่คาดหวัง (Expected scale)
   - เทคโนโลยีที่ต้องการใช้ (Tech stack)

3. **ตรวจสอบโครงสร้างทีม (Review the Blueprint)**
   Agent จะนำเสนอโครงสร้างทีมที่เหมาะสมสำหรับโปรเจกต์ (เช่น "Full-stack Engineer + QA Reviewer") ให้คุณทำการยืนยัน (Approve) หรือขอปรับเปลี่ยนแก้ไขทีมได้ตามต้องการ

4. **สร้างโครงสร้างไฟล์ (Generation)**
   Agent จะทำการคัดลอกไฟล์ที่จำเป็นจาก `catalog` ของ Factory ไปยังโฟลเดอร์ `.gemini` และ `docs/` ในโปรเจกต์เป้าหมายของคุณ
   - ไฟล์ `SKILL.md` ที่เฉพาะเจาะจงสำหรับโปรเจกต์จะถูกสร้างขึ้น
   - ไฟล์ `<RULE>` ที่เป็นกฎส่วนกลางจะถูกฉีดเข้าไปในโปรเจกต์

5. **เริ่มการพัฒนา (Start Development)**
   เมื่อขั้นตอนการเตรียมความพร้อมเสร็จสิ้น คุณสามารถเริ่มทำงานตามรายการ Task ในไฟล์ `TASK_BOARD.md` ได้ทันที
