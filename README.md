# Onealf Social Network

---

## 🇧🇷 Português (pt-BR)

### Sobre o Projeto

**Onealf Social Network** é uma rede social web desenvolvida com **Django 5**, permitindo que usuários se registrem, publiquem posts com imagens, interajam por meio de curtidas e comentários, e conversem em tempo real por mensagens privadas.

### Funcionalidades

- 👤 **Cadastro e autenticação** de usuários
- 🖼️ **Perfil personalizável** com foto e bio
- 📝 **Criação, edição e visualização de posts** com suporte a imagens
- ❤️ **Curtidas** nos posts (toggle like/unlike)
- 💬 **Comentários** nos posts
- 📩 **Chat privado** entre usuários cadastrados
- 🔒 Proteção por autenticação em rotas sensíveis
- ☁️ Upload de mídia via **Cloudinary**
- 🚀 Deploy configurado para **Render**

### Tecnologias Utilizadas

| Tecnologia | Versão |
|---|---|
| Python | 3.11 |
| Django | 5.2.3 |
| Gunicorn | 23.0.0 |
| Whitenoise | 6.9.0 |
| Cloudinary | 1.44.1 |
| Pillow | 11.3.0 |
| django-widget-tweaks | 1.5.0 |
| dj-database-url | 3.0.1 |

### Estrutura do Projeto

```
onealf-social-network/
├── core/               # App principal (models, views, forms, urls)
│   ├── models.py       # Perfil, Post, Comentario, Curtida, Mensagem
│   ├── views.py        # Lógica de negócio e rotas
│   ├── forms.py        # Formulários Django
│   ├── urls.py         # Rotas do app core
│   └── signals.py      # Sinais (ex: criação automática de perfil)
├── onealf/             # Configurações do projeto Django
├── templates/          # Templates HTML base
├── static/             # Arquivos estáticos (CSS, JS, imagens)
├── requirements.txt    # Dependências Python
├── render.yaml         # Configuração de deploy no Render
└── manage.py
```

### Como Rodar Localmente

**Pré-requisitos:** Python 3.11+, pip

```bash
# 1. Clone o repositório
git clone https://github.com/andreluizyz/onealf-social-network.git
cd onealf-social-network

# 2. Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Aplique as migrações
python manage.py migrate

# 5. Inicie o servidor de desenvolvimento
python manage.py runserver
```

Acesse em: [http://localhost:8000](http://localhost:8000)

### Variáveis de Ambiente

| Variável | Descrição |
|---|---|
| `SECRET_KEY` | Chave secreta do Django |
| `DATABASE_URL` | URL de conexão com o banco de dados (PostgreSQL em produção) |
| `CLOUDINARY_URL` | URL de configuração do Cloudinary para upload de mídia |

> Em desenvolvimento, sem `DATABASE_URL` definida, o projeto usa **SQLite** automaticamente.

### Deploy no Render

O projeto está configurado para deploy automático no [Render](https://render.com) via `render.yaml`. Basta conectar o repositório e configurar as variáveis de ambiente acima no painel do Render.

---

## 🇺🇸 English

### About the Project

**Onealf Social Network** is a web-based social network built with **Django 5**, allowing users to register, create posts with images, interact through likes and comments, and chat privately with other users.

### Features

- 👤 **User registration and authentication**
- 🖼️ **Customizable profile** with photo and bio
- 📝 **Create, edit, and view posts** with optional image upload
- ❤️ **Likes** on posts (toggle like/unlike)
- 💬 **Comments** on posts
- 📩 **Private chat** between registered users
- 🔒 Login-required protection on sensitive routes
- ☁️ Media uploads via **Cloudinary**
- 🚀 Deployment configured for **Render**

### Tech Stack

| Technology | Version |
|---|---|
| Python | 3.11 |
| Django | 5.2.3 |
| Gunicorn | 23.0.0 |
| Whitenoise | 6.9.0 |
| Cloudinary | 1.44.1 |
| Pillow | 11.3.0 |
| django-widget-tweaks | 1.5.0 |
| dj-database-url | 3.0.1 |

### Project Structure

```
onealf-social-network/
├── core/               # Main app (models, views, forms, urls)
│   ├── models.py       # Perfil, Post, Comentario, Curtida, Mensagem
│   ├── views.py        # Business logic and route handlers
│   ├── forms.py        # Django forms
│   ├── urls.py         # Core app URL routes
│   └── signals.py      # Signals (e.g., auto profile creation)
├── onealf/             # Django project settings
├── templates/          # Base HTML templates
├── static/             # Static assets (CSS, JS, images)
├── requirements.txt    # Python dependencies
├── render.yaml         # Render deployment config
└── manage.py
```

### Running Locally

**Prerequisites:** Python 3.11+, pip

```bash
# 1. Clone the repository
git clone https://github.com/andreluizyz/onealf-social-network.git
cd onealf-social-network

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations
python manage.py migrate

# 5. Start the development server
python manage.py runserver
```

Open your browser at: [http://localhost:8000](http://localhost:8000)

### Environment Variables

| Variable | Description |
|---|---|
| `SECRET_KEY` | Django secret key |
| `DATABASE_URL` | Database connection URL (PostgreSQL in production) |
| `CLOUDINARY_URL` | Cloudinary configuration URL for media uploads |

> In development, if `DATABASE_URL` is not set, the project automatically uses **SQLite**.

### Deploying on Render

The project is configured for automatic deployment on [Render](https://render.com) via `render.yaml`. Simply connect the repository and set the environment variables above in the Render dashboard.

---

## Models

| Model | Description |
|---|---|
| `Perfil` | Extends Django's `User` with profile photo and bio |
| `Post` | A post with title, content, optional image, and author |
| `Comentario` | Comment on a post, linked to a `Perfil` |
| `Curtida` | Like on a post (unique per user per post) |
| `Mensagem` | Private message between two users |

## URL Routes

| URL | View | Description |
|---|---|---|
| `/` | `home` | Feed with all posts |
| `/register/` | `register` | User registration |
| `/login/` | `LoginView` | Login |
| `/logout/` | `LogoutView` | Logout |
| `/perfil/<username>/` | `perfil` | User profile page |
| `/editar_perfil/<username>/` | `editar_perfil` | Edit profile |
| `/criar_post/` | `criar_post` | Create a new post |
| `/post/<id>/` | `ver_post` | View post + comments |
| `/editar_post/<id>/` | `editar_post` | Edit a post |
| `/post/<id>/curtir/` | `curtir_post` | Toggle like on post |
| `/mensagens/` | `lista_usuarios` | List users to chat with |
| `/chat/<username>/` | `chat_com_usuario` | Private chat with a user |
| `/sobre/` | `sobre` | About page |

---

*Made with ❤️ using Django*
