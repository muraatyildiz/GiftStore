# GiftStore

GiftStore is a full-stack gift shop application powered by a **Nuxt.js frontend** and a **Flask backend**. It supports user authentication, product management, and integrates OpenAI to generate automatic product description.

---

## Live Demo

- **Frontend**: [https://gift-store-three.vercel.app/](https://gift-store-three.vercel.app/)
- **Backend API**: [https://gift-shop-backend-8g7v.onrender.com](https://gift-shop-backend-8g7v.onrender.com)


---

## Folder Structure
<pre> 
GiftStore/
├── Backend/
│   ├── uploads
│   ├── app.py
│   ├── auth.py
│   ├── dbconn.py
│   ├── fileUpload.py
│   ├── homePage.py
│   ├── openAi.py
│   └── product.py
├── Frontend/
│   ├── assets
│   ├── layouts
│   ├── middleware
│   ├── pages
│   ├── plugins
│   ├── static
│   ├── store
│   ├── nuxt.config.js
│   └── package.json
├── README.md
└── render.yaml

</pre>


---

##  Local Development

### Frontend (Nuxt.js)

1.  Navigate to frontend:
 
    cd ../Frontend

2. Install dependencies:

    npm install

3. Run the frontend:

   npm run dev

Visit: http://localhost:3000


###  Backend (Flask + MongoDB + OpenAI)

1. Navigate to backend directory:
   ```bash
   cd Backend

2. Create virtual environment and install packages:

   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt

3. Create a .env file:

   DATABASE_LINK=your_mongodb_uri
   OPENAI_API_KEY=your_openai_api_key
   SECRET_KEY=your_secret

4. Run the backend:

   python app.py


##  Author
Murat Yildiz
Full-stack Software Developer
GitHub : [https://github.com/muraatyildiz](https://github.com/muraatyildiz)