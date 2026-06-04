def show_custom_spinner(text):
    return f"""
    <style>
    .custom-popup-overlay {{
        position: fixed;
        top: 0; left: 0; width: 100vw; height: 100vh;
        background-color: rgba(0, 0, 0, 0.4);
        z-index: 999999;
        display: flex;
        justify-content: center;
        align-items: center;
        backdrop-filter: blur(3px);
    }}
    .custom-popup-content {{
        background-color: var(--secondary-background-color, #ffffff);
        padding: 40px 60px;
        border-radius: 16px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.3);
        text-align: center;
        border: 1px solid var(--border-color, #e0e0e0);
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 20px;
    }}
    .spinner-circle {{
        width: 50px;
        height: 50px;
        border: 5px solid var(--primary-color, #ff4b4b);
        border-bottom-color: transparent;
        border-radius: 50%;
        display: inline-block;
        box-sizing: border-box;
        animation: rotation 1s linear infinite;
    }}
    @keyframes rotation {{
        0% {{ transform: rotate(0deg); }}
        100% {{ transform: rotate(360deg); }}
    }}
    </style>
    <div class="custom-popup-overlay">
        <div class="custom-popup-content">
            <div class="spinner-circle"></div>
            <h3 style="margin:0;">{text}</h3>
        </div>
    </div>
    """
