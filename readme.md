# 🎉 Giveaway Helper Telegram Bot  

Your ultimate tool for managing **giveaways**, broadcasting messages, and effortlessly maintaining **channel and user data**!  

---

## 🔑 **Required Variables**  

Before you begin, ensure you have the following:  

- **`BOT_TOKEN`** 🛠: Obtain your bot token by creating a bot with [@BotFather](https://t.me/BotFather).  
- **`API_ID`** 📱: Get it from [my.telegram.org](https://my.telegram.org).  
- **`API_HASH`** 🔑: Get it from [my.telegram.org](https://my.telegram.org).  
- **`DB_URI`** 🗄️: Your MongoDB URI to connect the bot to the database.  
- **`DB_NAME`** 📂: Name of your MongoDB database.  
- **`ADMIN_IDS`** 👑: List of Telegram user IDs of administrators with access to admin-only commands.  

---

## 🌟 **Features**  

### 🔗 **Channel Management**  
- ➕ Add or ➖ Remove channels with simple commands.  
- Supports **private** and **public** channels.  
- Automatically removes inaccessible channels during broadcasts to keep the database clean and updated.  

### ✉️ **Message Broadcasting**  
- Effortlessly broadcast messages to **all users and channels**.  
- Automatically handles blocked or inactive users and removes them from the database.  

### 👥 **User Tracking**  
- Automatically tracks new users who start the bot.  
- Removes **inactive** or **blocked** users to maintain an active user base.  

### 🚨 **Admin Notifications**  
- Notifies admins about **channel additions/removals**, keeping them informed of the bot's activities.  

---

## 🛠 **Setup Instructions**  

1. **Clone the Repository**  
   Clone the repository to your local environment:  
   ```bash
   git clone <repository-link>
   cd <repository-name>

## 🛠 Setup Instructions
1. **Clone the Repository**: Clone the repository to your local environment.
2. **Set Environment Variables**: Add required variables in a `.env` file or set them directly in your environment.
3. **Run the Bot**: Start the bot by executing:
   ```bash
   python main.py
## 📚 Commands

### User Commands
- **`/start`**: Start the bot and track the user.
- **`/add`**: Add the current channel or group to the database.
- **`/rem`**: Remove the current channel or group from the database.

### Admin Commands
- **`/users`**: View the total user count.
- **`/channels`**: View the list of all channels with their names and invite links.
- **`/broadcast`**: Broadcast a message to all users. Use this by replying to a message with the `/broadcast` command.
- **`/send`**: Forward a specific message to all channels in the database. Use by replying to a message with `/send`.
