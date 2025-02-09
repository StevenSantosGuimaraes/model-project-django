# 📦 ERP System - Documentação dos Aplicativos

Este projeto é um ERP modular desenvolvido em Django, estruturado em diferentes aplicativos para melhor organização e escalabilidade.

## 📂 Estrutura dos Aplicativos

### 1️⃣ **API** (`api/`)

📌 **Objetivo:**  
Fornece uma interface de comunicação baseada em **REST API** para permitir integração com frontend, mobile e sistemas externos.

🔹 **Principais funcionalidades:**

- Exposição de endpoints via **Django Rest Framework (DRF)**.
- Autenticação e autorização (**JWT, Token ou Sessão**).
- Endpoints para CRUD de diferentes entidades do sistema.

---

### 2️⃣ **Core** (`core/`)

📌 **Objetivo:**  
Módulo central do sistema, contendo modelos e funcionalidades compartilhadas entre os outros módulos.

🔹 **Principais funcionalidades:**

- Modelos básicos como **Usuário, Empresa, Endereço**.
- **Configurações do sistema e permissões**.
- **Utilitários e mixins** usados por outros aplicativos.

---

### 3️⃣ **CRM** (`crm/`)

📌 **Objetivo:**  
Gerencia o **relacionamento com clientes** e **gestão comercial**.

🔹 **Principais funcionalidades:**

- Cadastro e gestão de **clientes e leads**.
- Histórico de **interações, e-mails e reuniões**.
- Controle de **propostas comerciais e oportunidades de venda**.
- **Follow-up e notificações** automáticas.

---

### 4️⃣ **FRM (Finance & Resource Management)** (`frm/`)

📌 **Objetivo:**  
Responsável pela **gestão financeira** da empresa.

🔹 **Principais funcionalidades:**

- **Faturamento e emissão de notas fiscais**.
- Controle de **contas a pagar e receber**.
- **Fluxo de caixa e controle de despesas**.
- Integração com **bancos e gateways de pagamento**.

---

### 5️⃣ **HRM (Human Resource Management)** (`hrm/`)

📌 **Objetivo:**  
Gerencia os recursos humanos e folha de pagamento.

🔹 **Principais funcionalidades:**

- Cadastro e gerenciamento de **funcionários**.
- Controle de **cargos, setores e departamentos**.
- **Folha de pagamento, férias e benefícios**.
- Registro de **ponto eletrônico e controle de jornada**.

---

### 6️⃣ **MRP (Manufacturing Resource Planning)** (`mrp/`)

📌 **Objetivo:**  
Focado no planejamento e controle da **produção industrial**.

🔹 **Principais funcionalidades:**

- **Ordens de produção** e controle de processos.
- Gestão de **matéria-prima e insumos**.
- **Planejamento de capacidade e demanda**.
- **Rastreamento da produção e indicadores de eficiência**.

---

### 7️⃣ **SCM (Supply Chain Management)** (`scm/`)

📌 **Objetivo:**  
Gerencia a **cadeia de suprimentos e logística** da empresa.

🔹 **Principais funcionalidades:**

- **Gestão de fornecedores e contratos**.
- **Pedidos de compra e recebimento de mercadorias**.
- **Controle de estoque e armazenagem**.
- **Logística de entrega e rastreamento de pedidos**.

---

## 🔧 **Tecnologias Utilizadas**

- **Django** como framework principal.
- **Django Rest Framework (DRF)** para API.
- **PostgreSQL ou SQLite** para banco de dados.
- **JWT ou Token Authentication** para autenticação.

## 📌 **Sobre o Projeto**

Este ERP foi desenvolvido para aprimorar habilidades em **Django, arquitetura de software e boas práticas de desenvolvimento**. Ele é modular e pode ser expandido conforme necessário.

---

> 📢 **Observação:** Esta documentação pode ser expandida para incluir detalhes sobre instalação, configuração e contribuição para o projeto.
