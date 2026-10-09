# Agents Factory (คู่มือภาษาไทย)

**Agents Factory** คือระบบ meta-system ที่ออกแบบมาเพื่อใช้งานร่วมกับ Antigravity 2.0 Agent Manager โดยมีหน้าที่หลักในการ กำหนดค่า (configure), ตรวจสอบ (validate) และจัดเตรียม (provision) ทีมวิศวกร AI สำหรับโปรเจกต์ใหม่ๆ 

แทนที่จะสร้างทุกอย่างแบบตายตัว Factory นี้จะสร้างโครงสร้าง Workspace ที่ปรับเปลี่ยนได้ตามขอบเขต (Scope), ความซับซ้อน (Complexity) และความเสี่ยง (Risk) ของแต่ละโปรเจกต์

## ปรัชญาในการออกแบบ (Philosophy)
- **ทีมที่มีขนาดเล็กแต่ทรงประสิทธิภาพ (Minimal Viable Intelligence):** สร้างทีม AI ที่มีขนาดเล็กที่สุดที่สามารถทำงานโปรเจกต์ให้สำเร็จและปลอดภัยได้จริง
- **การประสานงานที่คงทน (Durable Coordination):** ใช้เอกสารสัญญาการทำงาน (Task Contracts), การรีวิวที่มีหลักฐานอ้างอิง, และการส่งมอบงานที่ชัดเจน แทนที่จะพึ่งพาแค่ประวัติการแชทเพียงอย่างเดียว
- **ระบบป้องกันความผิดพลาด (Fail-Safes):** มีการจำกัดรอบการแก้ไข (Bounded repair loops), มีระบบยกระดับการตัดสินใจไปสู่มนุษย์ (Escalation paths) และมีประตูตรวจสอบคุณภาพ (Quality gates) ที่ชัดเจน

## การใช้งาน (Usage)

ดูรายละเอียดขั้นตอนได้ที่ [วิธีเตรียมความพร้อมสำหรับโปรเจกต์ (How to Prepare a Project)](docs/HOW_TO_PREPARE_A_PROJECT_TH.md)

## โครงสร้าง Repository (Repository Structure)
- `templates/` — ไฟล์ Markdown แม่แบบสำหรับ Specs, Architectures, การบันทึกการตัดสินใจ ฯลฯ
- `catalog/` — ศูนย์รวมของ Agent Roles, Skills, Rules, และ Quality Gates ทั้งหมด
- `factory/` — ลอจิกหลักในการเตรียมความพร้อม (Intake, Discovery, Classification, Team Generation)
- `schemas/` — JSON Schemas สำหรับกำหนดโครงสร้างของ Factory contracts
- `docs/` — คู่มือการใช้งานและเอกสารอธิบายสถาปัตยกรรมระบบ

## การทำงาน (Execution)

Agents Factory ใช้ฟีเจอร์พื้นฐานของ Antigravity 2.0 (เช่น Skills, Rules, Artifacts, Subagents) 
หากโปรเจกต์ใดจำเป็นต้องใช้ State Machine แบบถาวร หรือมีการรันแบบ Distributed ก็สามารถปรับไปใช้ External Orchestrator ได้ (อ่านเพิ่ม: [Native vs Orchestrator](docs/NATIVE_VS_ORCHESTRATOR.md))
