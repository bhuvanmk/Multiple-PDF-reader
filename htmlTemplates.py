css = '''
<style>
.chat-message {
    padding: 1rem 1.5rem;
    border-radius: 12px;
    margin-bottom: 1rem;
    display: flex;
    align-items: flex-start;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    transition: background-color 0.3s ease;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.chat-message.user {
    background: linear-gradient(135deg, #3b82f6, #06b6d4);
}

.chat-message.bot {
    background: linear-gradient(135deg, #6366f1, #8b5cf6);
}

.chat-message .avatar {
    flex-shrink: 0;
    margin-right: 1rem;
}

.chat-message .avatar img {
    max-width: 60px;
    max-height: 60px;
    border-radius: 50%;
    object-fit: cover;
    border: 2px solid #38bdf8; /* light blue border */
}

.chat-message .message {
    flex: 1;
    padding: 0.5rem 0;
    color: #f1f5f9;
    font-size: 0.95rem;
    line-height: 1.5;
}

.chat-message.user:hover,
.chat-message.bot:hover {
    background: linear-gradient(135deg, #60a5fa, #22d3ee);
}
</style>
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.ibb.co/cN0nmSj/Screenshot-2023-05-28-at-02-37-21.png" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://i.ibb.co/rdZC7LZ/Photo-logo-1.png">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''