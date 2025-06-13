<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Oh Seoung Jong - UNIONMADE Portfolio (Perfect Blur & Mouse Spotlight)</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.4.0/css/all.min.css">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600;700;800;900&family=Inter:wght@300;400;500;600;700;800;900&display=swap');
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Inter', sans-serif;
            overflow-x: hidden;
            background: #000000;
            color: #ffffff;
            cursor: none;
        }

        /* Custom Cursor */
        .custom-cursor {
            position: fixed;
            width: 20px;
            height: 20px;
            background: radial-gradient(circle, rgba(255, 215, 0, 0.8) 0%, rgba(255, 215, 0, 0.4) 50%, transparent 100%);
            border-radius: 50%;
            pointer-events: none;
            z-index: 9998;
            mix-blend-mode: screen;
            transition: transform 0.1s ease;
        }

        /* Mouse Spotlight Effect */
        .mouse-spotlight {
            position: fixed;
            width: 400px;
            height: 400px;
            background: radial-gradient(circle, rgba(255, 255, 255, 0.1) 0%, rgba(255, 255, 255, 0.05) 30%, rgba(255, 215, 0, 0.02) 50%, transparent 70%);
            border-radius: 50%;
            pointer-events: none;
            z-index: 9997;
            mix-blend-mode: overlay;
            transition: transform 0.2s ease;
            transform: translate(-50%, -50%);
        }

        /* Theater Curtain Effect */
        .theater-curtain {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 10000;
            background: linear-gradient(135deg, #8B0000 0%, #DC143C 25%, #B22222 50%, #8B0000 75%, #A0252F 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 2s ease-in-out;
        }

        .theater-curtain.opening {
            clip-path: polygon(0 0, 48% 0, 48% 100%, 0 100%, 52% 0, 100% 0, 100% 100%, 52% 100%);
            opacity: 0;
        }

        .curtain-text {
            font-family: 'Playfair Display', serif;
            font-size: 4rem;
            font-weight: 900;
            color: #FFD700;
            text-shadow: 0 0 30px rgba(255, 215, 0, 0.8);
            letter-spacing: 0.2em;
            animation: glow 2s ease-in-out infinite alternate;
        }

        @keyframes glow {
            from { text-shadow: 0 0 30px rgba(255, 215, 0, 0.8); }
            to { text-shadow: 0 0 50px rgba(255, 215, 0, 1), 0 0 70px rgba(255, 215, 0, 0.8); }
        }

        /* Theater Stage Background */
        .theater-stage {
            background: radial-gradient(ellipse at center, #1a1a2e 0%, #0f0f23 40%, #000000 100%);
            position: relative;
            overflow: hidden;
        }

        .theater-stage::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: 
                linear-gradient(45deg, transparent 40%, rgba(255, 215, 0, 0.05) 50%, transparent 60%),
                radial-gradient(circle at 20% 80%, rgba(255, 215, 0, 0.1) 0%, transparent 50%),
                radial-gradient(circle at 80% 20%, rgba(255, 215, 0, 0.1) 0%, transparent 50%);
            pointer-events: none;
        }

        /* Spotlight Effects */
        .spotlight {
            position: absolute;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(255, 255, 255, 0.1) 0%, rgba(255, 255, 255, 0.05) 30%, transparent 70%);
            pointer-events: none;
            animation: spotlight-move 10s ease-in-out infinite;
        }

        .spotlight-1 {
            width: 800px;
            height: 800px;
            top: -200px;
            left: -200px;
            animation-delay: 0s;
        }

        .spotlight-2 {
            width: 600px;
            height: 600px;
            top: 50%;
            right: -200px;
            animation-delay: 3s;
        }

        @keyframes spotlight-move {
            0%, 100% { transform: translate(0, 0) scale(1); }
            25% { transform: translate(100px, 50px) scale(1.1); }
            50% { transform: translate(-50px, 100px) scale(0.9); }
            75% { transform: translate(80px, -30px) scale(1.05); }
        }

        /* Section Blur Effects */
        .section {
            transition: filter 0.3s ease, transform 0.3s ease;
            transform: translateZ(0);
        }

        .section.blur-light {
            filter: blur(2px);
        }

        .section.blur-medium {
            filter: blur(4px);
        }

        .section.blur-heavy {
            filter: blur(8px);
        }

        .section.active {
            filter: blur(0px);
        }

        .hero-section {
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            position: relative;
        }
        
        .intp-badge {
            position: absolute;
            top: 30px;
            right: 30px;
            background: linear-gradient(135deg, #FFD700, #FFA500);
            color: #000;
            padding: 12px 24px;
            border-radius: 25px;
            font-weight: 700;
            font-size: 16px;
            box-shadow: 0 8px 25px rgba(255, 215, 0, 0.4);
            border: 2px solid rgba(255, 215, 0, 0.6);
        }
        
        .hero-image {
            width: 600px;
            height: 600px;
            border-radius: 100%;
            object-fit: auto;
            border: 0px solid #FFD700;
            box-shadow: 
                0 0 50px rgba(255, 215, 0, 0.6),
                inset 0 0 50px rgba(255, 215, 0, 0.1);
            transition: all 1s ease;
            margin-bottom: 40px;
        }
        
        .hero-image:hover {
            transform: scale(1.1);
            box-shadow: 
                0 0 80px rgba(255, 215, 0, 0.8),
                inset 0 0 80px rgba(255, 215, 0, 0.2);
        }
        
        .intro-text {
            text-align: center;
            font-size: 20px;
            line-height: 1.8;
            max-width: 700px;
            margin: 0 auto 50px;
            color: #e0e0e0;
            text-shadow: 0 2px 10px rgba(0, 0, 0, 0.5);
        }
        
        .tools-section {
            display: flex;
            justify-content: center;
            gap: 30px;
            margin-top: 30px;
            flex-wrap: wrap;
            padding: 0 20px;
        }
        
        .tool-icon {
            width: 90px;
            height: 90px;
            border-radius: 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.4s ease;
            background: linear-gradient(135deg, rgba(255, 215, 0, 0.1), rgba(255, 215, 0, 0.05));
            border: 1px solid rgba(255, 217, 0, 0.698);
            backdrop-filter: blur(10px);
            position: relative;
            overflow: hidden;
            animation: wave-float 4s ease-in-out infinite;
        }

        /* Wave Animation for Icons */
        .tool-icon:nth-child(1) { animation-delay: 0s; }
        .tool-icon:nth-child(2) { animation-delay: 0.5s; }
        .tool-icon:nth-child(3) { animation-delay: 1s; }
        .tool-icon:nth-child(4) { animation-delay: 1.5s; }
        .tool-icon:nth-child(5) { animation-delay: 2s; }
        .tool-icon:nth-child(6) { animation-delay: 2.5s; }
        .tool-icon:nth-child(7) { animation-delay: 3s; }

        @keyframes wave-float {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-15px); }
        }

        .tool-icon::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: linear-gradient(45deg, transparent, rgba(255, 215, 0, 0.1), transparent);
            transform: rotate(45deg);
            transition: all 0.4s ease;
            opacity: 0;
        }
        
        .tool-icon:hover::before {
            opacity: 1;
            animation: shimmer 0.8s ease-in-out;
        }

        @keyframes shimmer {
            0% { transform: translateX(-100%) translateY(-100%) rotate(45deg); }
            100% { transform: translateX(100%) translateY(100%) rotate(45deg); }
        }
        
        .tool-icon img {
            width: 60px;
            height: 60px;
            object-fit: contain;
            z-index: 1;
        }
        
        .tool-icon:hover {
            transform: scale(1.15) translateY(-25px);
            box-shadow: 0 20px 40px rgba(255, 215, 0, 0.4);
            border-color: rgba(255, 215, 0, 0.8);
            animation-play-state: paused;
        }
        
        .about-section {
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            position: relative;
            padding: 100px 0;
        }
        
        .about-content {
            display: flex;
            align-items: center;
            gap: 100px;
            max-width: 1400px;
            width: 100%;
            padding: 0 60px;
        }
        
        .about-text {
            flex: 1;
        }
        
        .about-title {
            font-family: 'Playfair Display', serif;
            font-size: 6rem;
            font-weight: 900;
            margin-bottom: 50px;
            color: #FFD700;
            text-shadow: 0 0 30px rgba(255, 215, 0, 0.5);
            line-height: 0.9;
        }
        
        .about-description {
            font-size: 24px;
            line-height: 2;
            color: #e0e0e0;
            text-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
        }
        
        .about-image {
            width: 500px;
            height: 600px;
            object-fit: cover;
            border-radius: 25px;
            border: 5px solid #FFD700;
            box-shadow: 
                0 0 50px rgba(255, 215, 0, 0.4),
                0 25px 50px rgba(0, 0, 0, 0.3);
            transition: all 0.5s ease;
        }
        
        .about-image:hover {
            transform: scale(1.05) rotate(2deg);
            box-shadow: 
                0 0 80px rgba(255, 215, 0, 0.6),
                0 40px 80px rgba(0, 0, 0, 0.4);
        }
        
        .unionmade-section {
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            position: relative;
            overflow: hidden;
            padding: 100px 0;
        }
        
        .unionmade-title {
            font-family: 'Playfair Display', serif;
            font-size: 10rem;
            font-weight: 900;
            color: #FFD700;
            text-align: center;
            letter-spacing: 0.2em;
            text-transform: uppercase;
            margin-bottom: 80px;
            text-shadow: 
                0 0 50px rgba(255, 215, 0, 0.8),
                0 0 100px rgba(255, 215, 0, 0.4);
            transition: all 0.3s ease;
        }
        
        .unionmade-title:hover {
            transform: scale(1.02);
            text-shadow: 
                0 0 80px rgba(255, 215, 0, 1),
                0 0 150px rgba(255, 215, 0, 0.6);
        }
        
        .projects-container {
            width: 100%;
            overflow: hidden;
            position: relative;
            height: 500px;
        }
        
        .projects-scroll {
            display: flex;
            gap: 40px;
            animation: scroll 25s linear infinite;
            width: max-content;
        }
        
        .project-item {
            width: 350px;
            height: 450px;
            border-radius: 20px;
            overflow: hidden;
            transition: all 0.4s ease;
            cursor: pointer;
            flex-shrink: 0;
            border: 3px solid rgba(255, 215, 0, 0.3);
            box-shadow: 0 15px 40px rgba(0, 0, 0, 0.4);
            position: relative;
        }

        .project-item::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(45deg, rgba(255, 215, 0, 0.1), transparent, rgba(255, 215, 0, 0.1));
            opacity: 0;
            transition: all 0.4s ease;
            z-index: 1;
        }

        .project-item:hover::before {
            opacity: 1;
        }
        
        .project-item:hover {
            transform: scale(1.1) translateY(-20px);
            border-color: rgba(255, 215, 0, 0.8);
            box-shadow: 
                0 25px 60px rgba(255, 215, 0, 0.3),
                0 15px 40px rgba(0, 0, 0, 0.5);
        }
        
        .project-item img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: all 0.4s ease;
        }
        
        .project-item:hover img {
            transform: scale(1.1);
            filter: brightness(1.2) contrast(1.1);
        }
        
        @keyframes scroll {
            0% { transform: translateX(0); }
            100% { transform: translateX(-50%); }
        }
        
        .make-cloth-section {
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            position: relative;
            padding: 100px 0;
        }
        
        .make-cloth-content {
            text-align: center;
            max-width: 900px;
            padding: 0 40px;
        }
        
        .make-cloth-title {
            font-family: 'Playfair Display', serif;
            font-size: 5rem;
            font-weight: 900;
            margin-bottom: 60px;
            letter-spacing: 0.1em;
            color: #FFD700;
            text-shadow: 0 0 40px rgba(255, 215, 0, 0.6);
        }
        
        .person-image {
            width: 700px;
            height: 700px;
            border-radius: 25px;
            margin: 0 auto 50px;
            overflow: hidden;
            border: 0px solid #FFD700;
            box-shadow: 
                0 0 50px rgba(255, 215, 0, 0.4),
                0 25px 50px rgba(0, 0, 0, 0.3);
            transition: all 0.5s ease;
        }

        .person-image img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
        
        .person-image:hover {
            transform: scale(1.05) rotate(-2deg);
            box-shadow: 
                0 0 80px rgba(255, 215, 0, 0.6),
                0 40px 80px rgba(0, 0, 0, 0.4);
        }
        
        .contact-info {
            font-size: 22px;
            line-height: 1.8;
            color: #e0e0e0;
            text-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
        }

        /* Show Ending Effect */
        .show-ending {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 9999;
            background: rgba(0, 0, 0, 0.95);
            display: none;
            align-items: center;
            justify-content: center;
            flex-direction: column;
        }

        .show-ending.active {
            display: flex;
            animation: fadeIn 2s ease-in-out;
        }

        .ending-curtain {
            position: absolute;
            top: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(135deg, #8B0000 0%, #DC143C 25%, #B22222 50%, #8B0000 75%, #A0252F 100%);
            clip-path: polygon(0 0, 0 0, 0 100%, 0 100%, 100% 0, 100% 0, 100% 100%, 100% 100%);
            animation: curtainClose 3s ease-in-out 1s forwards;
        }

        .ending-text {
            font-family: 'Playfair Display', serif;
            font-size: 6rem;
            font-weight: 900;
            color: #FFD700;
            text-shadow: 0 0 50px rgba(255, 215, 0, 0.8);
            letter-spacing: 0.3em;
            opacity: 0;
            animation: textAppear 2s ease-in-out 4s forwards;
            z-index: 1;
        }

        .ending-subtitle {
            font-family: 'Inter', sans-serif;
            font-size: 1.5rem;
            color: #e0e0e0;
            margin-top: 30px;
            opacity: 0;
            animation: textAppear 2s ease-in-out 5s forwards;
            z-index: 1;
        }

        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }

        @keyframes curtainClose {
            0% { clip-path: polygon(0 0, 0 0, 0 100%, 0 100%, 100% 0, 100% 0, 100% 100%, 100% 100%); }
            100% { clip-path: polygon(0 0, 48% 0, 48% 100%, 0 100%, 52% 0, 100% 0, 100% 100%, 52% 100%); }
        }

        @keyframes textAppear {
            from { opacity: 0; transform: translateY(30px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* Fade-in animations */
        .fade-in {
            opacity: 0;
            transform: translateY(50px);
            transition: all 1s ease;
        }
        
        .fade-in.visible {
            opacity: 1;
            transform: translateY(0);
        }

        /* Responsive Design */
        @media (max-width: 768px) {
            .curtain-text { font-size: 2.5rem; }
            .hero-image { width: 250px; height: 250px; }
            .about-content { flex-direction: column; gap: 50px; }
            .about-title { font-size: 4rem; text-align: center; }
            .about-image { width: 350px; height: 420px; }
            .unionmade-title { font-size: 6rem; }
            .make-cloth-title { font-size: 3rem; }
            .person-image { width: 300px; height: 300px; }
            .tool-icon { width: 70px; height: 70px; }
            .tool-icon img { width: 45px; height: 45px; }
            .ending-text { font-size: 3rem; }
            .ending-subtitle { font-size: 1.2rem; }
            
            body { cursor: default; }
            .custom-cursor, .mouse-spotlight { display: none; }
        }
    </style>
</head>
<body>
    <!-- Custom Cursor -->
    <div class="custom-cursor" id="customCursor"></div>
    <div class="mouse-spotlight" id="mouseSpotlight"></div>

    <!-- Theater Curtain -->
    <div class="theater-curtain" id="curtain">
        <div class="curtain-text">UNIONMADE</div>
    </div>

    <!-- Show Ending -->
    <div class="show-ending" id="showEnding">
        <div class="ending-curtain"></div>
        <div class="ending-text">THE END</div>
        <div class="ending-subtitle">지금까지 유니온메이드 대표 오승종이었습니다</div>
    </div>

    <!-- Hero Section -->
    <section class="hero-section theater-stage section" id="section1">
        <div class="spotlight spotlight-1"></div>
        <div class="spotlight spotlight-2"></div>
        
        <div class="intp-badge">UNIONMADE 대표 오승종</div>
        
        <img src="8.jpg" alt="Profile Picture" class="hero-image">
        
        <p class="intro-text">
            안녕하세요! 세상을 즐기는 디자이너 유니온메이드 대표 오승종입니다.<br>
            다양한 분야에서의 경험을 바탕으로 독창적이고 의미 있는 디자인을 만들어 나가고 있습니다.
        </p>
        
        <div class="tools-section">
            <div class="tool-icon">
                <img src="1.png" alt="Tool 1">
            </div>
            <div class="tool-icon">
                <img src="2.png" alt="Tool 2">
            </div>
            <div class="tool-icon">
                <img src="3.png" alt="Tool 3">
            </div>
            <div class="tool-icon">
                <img src="4.png" alt="Tool 4">
            </div>
            <div class="tool-icon">
                <img src="5.png" alt="Tool 5">
            </div>
            <div class="tool-icon">
                <img src="6.png" alt="Tool 6">
            </div>
            <div class="tool-icon">
                <img src="7.png" alt="Tool 7">
            </div>
        </div>
    </section>

    <!-- About Section -->
    <section class="about-section theater-stage section" id="section2">
        <div class="spotlight spotlight-1"></div>
        <div class="about-content">
            <div class="about-text">
                <h2 class="about-title">ABOUT<br>ME</h2>
                <p class="about-description">
                    지속적인 디자인으로 세상을 바꿀려고합니다.<br>
                    사용자의 니즈를 파악하고<br>
                    최적의 솔루션을 제공하여<br>
                    브랜드의 가치를 높이는 것이<br>
                    저의 목표입니다.
                </p>
            </div>
            <img src="9.png" alt="About Me Image" class="about-image">
        </div>
    </section>

    <!-- UNIONMADE Section -->
    <section class="unionmade-section theater-stage section" id="section3">
        <div class="spotlight spotlight-2"></div>
        <h1 class="unionmade-title">UNIONMADE</h1>
        <div class="projects-container">
            <div class="projects-scroll">
                <div class="project-item">
                    <img src="10.png" alt="UNIONMADE Project 1">
                </div>
                <div class="project-item">
                    <img src="11.png" alt="UNIONMADE Project 2">
                </div>
                <div class="project-item">
                    <img src="12.png" alt="UNIONMADE Project 3">
                </div>
                <div class="project-item">
                    <img src="13.png" alt="UNIONMADE Project 4">
                </div>
                <div class="project-item">
                    <img src="14.png" alt="UNIONMADE Project 5">
                </div>
                <div class="project-item">
                    <img src="15.png" alt="UNIONMADE Project 6">
                </div>
                <div class="project-item">
                    <img src="16.png" alt="UNIONMADE Project 7">
                </div>
                <div class="project-item">
                    <img src="17.png" alt="UNIONMADE Project 8">
                </div>
                <!-- 반복을 위한 복사본 -->
                <div class="project-item">
                    <img src="10.png" alt="UNIONMADE Project 1">
                </div>
                <div class="project-item">
                    <img src="11.png" alt="UNIONMADE Project 2">
                </div>
                <div class="project-item">
                    <img src="12.png" alt="UNIONMADE Project 3">
                </div>
                <div class="project-item">
                    <img src="13.png" alt="UNIONMADE Project 4">
                </div>
            </div>
        </div>
    </section>

    <!-- Make Cloth Section -->
    <section class="make-cloth-section theater-stage section" id="section4">
        <div class="spotlight spotlight-1"></div>
        <div class="make-cloth-content">
            <h2 class="make-cloth-title">MAKE CLOTH</h2>
            <div class="person-image">
                <img src="25.png" alt="Make Cloth Image">
            </div>
            <div class="contact-info">
                <p>TWILIGHT321@NAVER.COM<br>
                UNIONMADE_vtg @ instagram</p>
            </div>
        </div>
    </section>

    <script>
        // Mouse cursor and spotlight effect
        const cursor = document.getElementById('customCursor');
        const spotlight = document.getElementById('mouseSpotlight');
        let mouseX = 0, mouseY = 0;
        
        document.addEventListener('mousemove', (e) => {
            mouseX = e.clientX;
            mouseY = e.clientY;
            
            cursor.style.left = mouseX + 'px';
            cursor.style.top = mouseY + 'px';
            
            spotlight.style.left = mouseX + 'px';
            spotlight.style.top = mouseY + 'px';
        });

        // Theater curtain opening effect
        window.addEventListener('load', () => {
            setTimeout(() => {
                document.getElementById('curtain').classList.add('opening');
                setTimeout(() => {
                    document.getElementById('curtain').style.display = 'none';
                }, 2000);
            }, 1500);
        });

        // Improved blur effect based on viewport visibility
        function updateBlurEffects() {
            const sections = document.querySelectorAll('.section');
            const viewportCenter = window.innerHeight / 2 + window.pageYOffset;
            
            sections.forEach((section, index) => {
                const rect = section.getBoundingClientRect();
                const sectionTop = rect.top + window.pageYOffset;
                const sectionBottom = sectionTop + rect.height;
                const sectionCenter = sectionTop + (rect.height / 2);
                
                // Calculate distance from viewport center to section center
                const distanceFromCenter = Math.abs(viewportCenter - sectionCenter);
                const maxDistance = window.innerHeight;
                
                // Remove all blur classes
                section.classList.remove('blur-light', 'blur-medium', 'blur-heavy', 'active');
                
                // Check if section is currently in viewport
                const isInViewport = (rect.top < window.innerHeight && rect.bottom > 0);
                
                if (isInViewport) {
                    // Section is in viewport - check how centered it is
                    const normalizedDistance = distanceFromCenter / maxDistance;
                    
                    if (normalizedDistance < 0.1) {
                        section.classList.add('active');
                    } else if (normalizedDistance < 0.3) {
                        section.classList.add('blur-light');
                    } else if (normalizedDistance < 0.6) {
                        section.classList.add('blur-medium');
                    } else {
                        section.classList.add('blur-heavy');
                    }
                } else {
                    // Section is not in viewport
                    if (rect.top > window.innerHeight) {
                        // Section is below viewport
                        section.classList.add('blur-medium');
                    } else if (rect.bottom < 0) {
                        // Section is above viewport
                        section.classList.add('blur-heavy');
                    }
                }
            });
        }

        // Throttle scroll events for better performance
        let scrollTimeout;
        window.addEventListener('scroll', () => {
            if (scrollTimeout) {
                clearTimeout(scrollTimeout);
            }
            scrollTimeout = setTimeout(updateBlurEffects, 10);
        });

        // Initial blur effect setup
        setTimeout(() => {
            updateBlurEffects();
        }, 3000);

        // Show ending trigger with longer delay
        let endingTriggered = false;
        let lastScrollTime = 0;
        let scrollEndTimeout;

        function checkForEnding() {
            const currentTime = Date.now();
            lastScrollTime = currentTime;
            
            // Clear previous timeout
            clearTimeout(scrollEndTimeout);
            
            // Set new timeout for 3 seconds after scrolling stops
            scrollEndTimeout = setTimeout(() => {
                if (!endingTriggered && Date.now() - lastScrollTime >= 3000) {
                    const scrollPosition = window.pageYOffset;
                    const documentHeight = document.documentElement.scrollHeight;
                    const windowHeight = window.innerHeight;
                    
                    // Trigger ending when user is at bottom and hasn't scrolled for 3 seconds
                    if (scrollPosition + windowHeight >= documentHeight - 100) {
                        endingTriggered = true;
                        document.getElementById('showEnding').classList.add('active');
                        
                        // Restart the show after 8 seconds
                        setTimeout(() => {
                            document.getElementById('showEnding').classList.remove('active');
                            window.scrollTo({ top: 0, behavior: 'smooth' });
                            endingTriggered = false;
                        }, 8000);
                    }
                }
            }, 3000);
        }

        window.addEventListener('scroll', checkForEnding);

        // Enhanced tool icon interactions
        document.querySelectorAll('.tool-icon').forEach(icon => {
            icon.addEventListener('click', () => {
                const originalAnimation = icon.style.animation;
                icon.style.animation = 'none';
                icon.style.transform = 'scale(1.3) rotate(360deg) translateY(-30px)';
                icon.style.boxShadow = '0 30px 60px rgba(255, 215, 0, 0.8)';
                setTimeout(() => {
                    icon.style.transform = '';
                    icon.style.boxShadow = '';
                    icon.style.animation = originalAnimation;
                }, 800);
            });
        });

        // Project item interactions
        document.querySelectorAll('.project-item').forEach(item => {
            item.addEventListener('click', () => {
                item.style.transform = 'scale(1.15) translateY(-30px) rotate(5deg)';
                item.style.zIndex = '1000';
                setTimeout(() => {
                    item.style.transform = '';
                    item.style.zIndex = '';
                }, 600);
            });
        });

        // Smooth scroll behavior
        document.documentElement.style.scrollBehavior = 'smooth';

        // Parallax effect for spotlights
        window.addEventListener('scroll', () => {
            const scrolled = window.pageYOffset;
            const spotlights = document.querySelectorAll('.spotlight');
            
            spotlights.forEach((spotlight, index) => {
                const speed = 0.3 + (index * 0.1);
                const yPos = scrolled * speed;
                spotlight.style.transform = `translateY(${yPos}px)`;
            });
        });

        // Cursor effects on hover
        document.querySelectorAll('.tool-icon, .project-item, .hero-image, .about-image, .person-image').forEach(element => {
            element.addEventListener('mouseenter', () => {
                cursor.style.transform = 'scale(2)';
                spotlight.style.transform = 'translate(-50%, -50%) scale(1.5)';
            });
            
            element.addEventListener('mouseleave', () => {
                cursor.style.transform = 'scale(1)';
                spotlight.style.transform = 'translate(-50%, -50%) scale(1)';
            });
        });
    </script>
</body>
</html>