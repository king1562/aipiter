<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EUNJI'S WEB PORTFOLIO</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Noto Sans KR', sans-serif;
        }
        .gradient-bg {
            background: linear-gradient(135deg, #013b06 0%, #000000 100%);
        }
        .hero-gradient {
            background: linear-gradient(-45deg, #013b06, #000000, #194e12, #1b2e02, #0c200d, #020303);
            background-size: 400% 400%;
            animation: gradientShift 8s ease infinite;
        }

        @keyframes gradientShift {
            0% {
                background-position: 0% 50%;
            }
            50% {
                background-position: 100% 50%;
            }
            100% {
                background-position: 0% 50%;
            }
        }
        .skill-icon {
            transition: transform 0.3s ease;
        }
        .skill-icon:hover {
            transform: scale(1.1);
        }
        .portfolio-item {
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .portfolio-item:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 25px rgba(0,0,0,0.15);
        }
        .section-title {
            position: relative;
            display: inline-block;
        }
        .section-title::after {
            content: '';
            position: absolute;
            bottom: -5px;
            left: 0;
            width: 100%;
            height: 3px;
            background: linear-gradient(90deg, #011b02 0%, #000000 100%);
            border-radius: 2px;
        }
        
        /* Skills infinite scroll animation - 개선된 반복 */
        .skills-container {
            overflow: hidden;
            position: relative;
        }
        .skills-scroll {
            display: flex;
            animation: infiniteScroll 25s linear infinite;
            white-space: nowrap;
            width: calc(200% + 32px);
        }
        .skills-scroll:hover {
            animation-play-state: paused;
        }
        @keyframes infiniteScroll {
            0% { transform: translateX(0); }
            100% { transform: translateX(-50%); }
        }
        
        /* BI BX fade animation - 크기 줄임 */
        .bi-bx-container {
            position: relative;
            height: 600px;
            overflow: hidden;
            border-radius: 0.7rem;
        }
        .bi-bx-slide {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            opacity: 0;
            transition: opacity 1s ease-in-out;
        }
        .bi-bx-slide.active {
            opacity: 1;
        }
        .bi-bx-slide img {
            width: 100%;
            height: 100%;
            object-fit: contain;
            background: #f8f9fa;
        }
        
        /* Video thumbnail styles - 세로 늘림 */
        .video-thumbnail {
            position: relative;
            cursor: pointer;
            overflow: hidden;
            border-radius: 0.5rem;
        }
        .video-thumbnail::before {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 50px;
            height: 50px;
            background: rgba(255, 255, 255, 0.9);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 2;
        }
        .video-thumbnail::after {
            content: '▶';
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            color: #333;
            font-size: 20px;
            z-index: 3;
        }
        .video-thumbnail:hover::before {
            background: rgba(255, 255, 255, 1);
        }
        
        /* Media title styling */
        .media-title {
            cursor: pointer;
            transition: all 0.3s ease;
            background: linear-gradient(45deg, #141414);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            font-weight: 600;
        }
        .media-title:hover {
            transform: translateY(-2px);
            text-shadow: 0 2px 10px rgba(62, 62, 62, 0.3);
        }
        
/* ETC Design Slider - 슬라이드 애니메이션 개선 */
.etc-slider-container {
    position: relative;
    overflow: hidden;
    border-radius: 0.5rem;
}

.etc-slides-wrapper {
    display: flex;
    transition: transform 0.6s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    width: 300%; /* 3개 슬라이드 * 100% */
}

.etc-slide {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1rem;
    width: 33.333%; /* 전체 너비의 1/3 */
    flex-shrink: 0;
}

.etc-nav-btn {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    background: rgba(255, 255, 255, 0.9);
    border: none;
    border-radius: 50%;
    width: 50px;
    height: 50px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: all 0.3s ease;
    z-index: 10;
    box-shadow: 0 4px 15px rgba(0,0,0,0.2);
}

.etc-nav-btn:hover {
    background: rgba(255, 255, 255, 1);
    transform: translateY(-50%) scale(1.1);
    box-shadow: 0 6px 20px rgba(0,0,0,0.3);
}

.etc-nav-btn:active {
    transform: translateY(-50%) scale(0.95);
}

.etc-prev {
    left: 15px;
}

.etc-next {
    right: 15px;
}

.etc-nav-btn i {
    font-size: 18px;
    color: #333;
}

/* 슬라이드 인디케이터 추가 */
.etc-indicators {
    position: absolute;
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    gap: 10px;
    z-index: 10;
}

.etc-indicator {
    width: 12px;
    height: 12px;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.5);
    cursor: pointer;
    transition: all 0.3s ease;
}

.etc-indicator.active {
    background: rgba(255, 255, 255, 0.9);
    transform: scale(1.2);
}

.etc-indicator:hover {
    background: rgba(255, 255, 255, 0.8);
}        /* Skill image styles */
        .skill-image {
            width: 100%;
            height: 100%;
            object-fit: contain;
            border-radius: 0.5rem;
        }
        
        /* Branding design image fix */
        .branding-image {
            width: 100%;
            height: 100%;
            object-fit: contain;
            background: #f8f9fa;
        }
        
/* INSTA TOON 3D 원통 회전 슬라이더 - 호버 시 그 자리에서 정지 */
.toon-container {
    position: relative;
    width: 100%;
    height: 600px;
    overflow: visible;
    border-radius: 1rem;
    background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    perspective: 1200px;
}

.toon-carousel {
    position: relative;
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    transform-style: preserve-3d;
    transform: rotateX(-15deg);
}

.toon-item {
    position: absolute;
    width: 160px;
    height: 213px;
    border-radius: 15px;
    overflow: hidden;
    transition: all 1s ease;
    cursor: pointer;
    box-shadow: 0 12px 35px rgba(0,0,0,0.4);
    transform-style: preserve-3d;
}

.toon-item img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

/* 호버 시 해당 아이템만 살짝 커지기 (위치는 그대로) */
.toon-item:hover {
    transform: scale(1.1) !important;
    box-shadow: 0 15px 40px rgba(0,0,0,0.6);
    z-index: 100;
}

/* 3D 원통 효과 */
.toon-item:nth-child(1) { transform: rotateY(0deg) translateZ(280px); }
.toon-item:nth-child(2) { transform: rotateY(40deg) translateZ(280px); }
.toon-item:nth-child(3) { transform: rotateY(80deg) translateZ(280px); }
.toon-item:nth-child(4) { transform: rotateY(120deg) translateZ(280px); }
.toon-item:nth-child(5) { transform: rotateY(160deg) translateZ(280px); }
.toon-item:nth-child(6) { transform: rotateY(200deg) translateZ(280px); }
.toon-item:nth-child(7) { transform: rotateY(240deg) translateZ(280px); }
.toon-item:nth-child(8) { transform: rotateY(280deg) translateZ(280px); }
.toon-item:nth-child(9) { transform: rotateY(320deg) translateZ(280px); }

.toon-carousel.rotating {
    animation: rotate3D 15s linear infinite;
}

/* 개별 아이템 호버 시 회전 일시정지 */
.toon-item:hover ~ .toon-carousel,
.toon-carousel:has(.toon-item:hover) {
    animation-play-state: paused;
}

@keyframes rotate3D {
    from {
        transform: rotateX(-15deg) rotateY(0deg);
    }
    to {
        transform: rotateX(-15deg) rotateY(360deg);
    }
}
</style>
</head>
<body class="bg-gray-50">
    <!-- Navigation -->
    <nav class="fixed top-0 w-full bg-white bg-opacity-80 backdrop-blur-sm z-50 shadow-sm">
        <div class="container mx-auto px-6 py-4">
            <div class="flex justify-between items-center">
                <div class="text-2xl font-bold text-gray-800">UNIONMADE</div>
                <div class="hidden md:flex space-x-8">
                    <a href="#about" class="text-gray-600 hover:text-gray-800 transition-colors">UNIONMADE</a>
                    <a href="#skills" class="text-gray-600 hover:text-gray-800 transition-colors">US ARMY</a>
                    <a href="#portfolio" class="text-gray-600 hover:text-gray-800 transition-colors">REMAKE</a>
                    <a href="#contact" class="text-gray-600 hover:text-gray-800 transition-colors">REPRINT</a>
                </div>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="hero-gradient min-h-screen flex items-center justify-center text-white">
        <div class="text-center px-6">
            <h1 class="text-6xl md:text-8xl font-bold mb-6">UNIONMADE<br>STORE</h1>
            <p class="text-xl md:text-2xl mb-8 opacity-90">유니온메이드는 복각 브랜드입니다 <br>실제 역사에 대한 옷들을 통해 구매자 분들에게 다가갑니다</p>
            <div class="flex justify-center space-x-4">
                <a href="#portfolio" class="bg-white text-gray-800 px-8 py-3 rounded-full font-semibold hover:bg-gray-100 transition-colors">구매하기</a>
                <a href="#contact" class="border border-white px-8 py-3 rounded-full font-semibold hover:bg-white hover:text-gray-800 transition-colors">연락하기</a>
            </div>
        </div>
    </section>

    <!-- About UNIONMADE Section -->
    <section id="about" class="py-20 bg-white">
        <div class="container mx-auto px-6">
            <div class="grid md:grid-cols-2 gap-12 items-center">
                <div class="text-center md:text-left">
                    <h2 class="section-title text-4xl font-bold text-gray-800 mb-8">UNIONMADE</h2>
                    <div class="w-80 h-80 mx-auto md:mx-0 mb-8 rounded-full overflow-hidden shadow-lg">
                        <img src="0.PNG" alt="Profile Image" class="w-full h-full object-cover">
                    </div>
                </div>
                <div class="space-y-6">
                    <h3 class="text-2xl font-bold text-gray-800">경험을 공유하는 UNIONMADE 입니다.</h3>
                    <p class="text-gray-600 font-semibold leading-relaxed">
                        저희는 실제 역사 WW1, WW2에 실전 착용된 옷들을 구매자 여러분들에게 선보입니다. 덕욱 저희는 실제 제품을 리메이크하여 조금더 
                        보편적으로 다다가고자 합니다. 저희는 과거와 현재를 옷이라는 매개체로 연결하고자합니다
                    </p>
                    <p class="text-gray-600 font-semibold leading-relaxed">
                        혼돈치는 세계에서 저희는 도전을 통해 최신 디자인 만들어 낼것이며  
                        사용자 경험을 최우선으로 하는 브랜드 입니다.
                    </p>
                    <div class="flex flex-wrap gap-4 pt-4">
                        <span class="bg-green-100 text-black-800 px-3 py-1 rounded-full text-sm">Ww1/Ww2</span>
                        <span class="bg-green-100 text-black-800 px-3 py-1 rounded-full text-sm">Us Army</span>
                        <span class="bg-green-100 text-black-800 px-3 py-1 rounded-full text-sm">Remake</span>
                        <span class="bg-green-100 text-black-800 px-3 py-1 rounded-full text-sm">Reprint</span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Skills Section -->
    <section id="skills" class="py-20 bg-gray-50">
        <div class="container mx-auto px-6">
            <h2 class="section-title text-4xl font-bold text-center text-gray-800 mb-16">US ARMY</h2>
            <div class="skills-container">
                <div class="skills-scroll">
                    <!-- 첫 번째 세트 -->
                    <div class="skill-icon text-center mx-8">
                        <div class="w-16 h-16 rounded-lg mx-auto mb-3 overflow-hidden">
                            <img src="1.PNG" alt="HTML" class="skill-image">
                        </div>
                        <span class="text-sm text-gray-600">200.000</span>
                    </div>
                    <div class="skill-icon text-center mx-8">
                        <div class="w-16 h-16 rounded-lg mx-auto mb-3 overflow-hidden">
                            <img src="2.PNG" alt="CSS" class="skill-image">
                        </div>
                        <span class="text-sm text-gray-600">300.000</span>
                    </div>
                    <div class="skill-icon text-center mx-8">
                        <div class="w-16 h-16 rounded-lg mx-auto mb-3 overflow-hidden">
                            <img src="3.PNG" alt="JavaScript" class="skill-image">
                        </div>
                        <span class="text-sm text-gray-600">300.000</span>
                    </div>
                    <div class="skill-icon text-center mx-8">
                        <div class="w-16 h-16 rounded-lg mx-auto mb-3 overflow-hidden">
                            <img src="4.png" alt="Figma" class="skill-image">
                        </div>
                        <span class="text-sm text-gray-600">350.000</span>
                    </div>
                    <div class="skill-icon text-center mx-8">
                        <div class="w-16 h-16 rounded-lg mx-auto mb-3 overflow-hidden">
                            <img src="5.png" alt="Photoshop" class="skill-image">
                        </div>
                        <span class="text-sm text-gray-600">400.000</span>
                    </div>
                    <div class="skill-icon text-center mx-8">
                        <div class="w-16 h-16 rounded-lg mx-auto mb-3 overflow-hidden">
                            <img src="6.png" alt="Illustrator" class="skill-image">
                        </div>
                        <span class="text-sm text-gray-600">300.000</span>
                    </div>
                    <div class="skill-icon text-center mx-8">
                        <div class="w-16 h-16 rounded-lg mx-auto mb-3 overflow-hidden">
                            <img src="7.png" alt="After Effects" class="skill-image">
                        </div>
                        <span class="text-sm text-gray-600">500.000</span>
                    </div>
                    <div class="skill-icon text-center mx-8">
                        <div class="w-16 h-16 rounded-lg mx-auto mb-3 overflow-hidden">
                            <img src="8.png" alt="Premiere Pro" class="skill-image">
                        </div>
                        <span class="text-sm text-gray-600">300.000</span>
                    </div>
                    <div class="skill-icon text-center mx-8">
                        <div class="w-16 h-16 rounded-lg mx-auto mb-3 overflow-hidden">
                            <img src="1.PNG" alt="HTML" class="skill-image">
                        </div>
                        <span class="text-sm text-gray-600">200.000</span>
                    </div>
                    <div class="skill-icon text-center mx-8">
                        <div class="w-16 h-16 rounded-lg mx-auto mb-3 overflow-hidden">
                            <img src="2.PNG" alt="CSS" class="skill-image">
                        </div>
                        <span class="text-sm text-gray-600">300.000</span>
                    </div>
                    <div class="skill-icon text-center mx-8">
                        <div class="w-16 h-16 rounded-lg mx-auto mb-3 overflow-hidden">
                            <img src="3.PNG" alt="JavaScript" class="skill-image">
                        </div>
                        <span class="text-sm text-gray-600">300.000</span>
                    </div>
                    <div class="skill-icon text-center mx-8">
                        <div class="w-16 h-16 rounded-lg mx-auto mb-3 overflow-hidden">
                            <img src="4.png" alt="Figma" class="skill-image">
                        </div>
                        <span class="text-sm text-gray-600">350.000</span>
                    </div>
                    <div class="skill-icon text-center mx-8">
                        <div class="w-16 h-16 rounded-lg mx-auto mb-3 overflow-hidden">
                            <img src="5.png" alt="Photoshop" class="skill-image">
                        </div>
                        <span class="text-sm text-gray-600">400.000</span>
                    </div>
                    <div class="skill-icon text-center mx-8">
                        <div class="w-16 h-16 rounded-lg mx-auto mb-3 overflow-hidden">
                            <img src="6.png" alt="Illustrator" class="skill-image">
                        </div>
                        <span class="text-sm text-gray-600">300.000</span>
                    </div>
                    <div class="skill-icon text-center mx-8">
                        <div class="w-16 h-16 rounded-lg mx-auto mb-3 overflow-hidden">
                            <img src="7.png" alt="After Effects" class="skill-image">
                        </div>
                        <span class="text-sm text-gray-600">500.000</span>
                    </div>
                    <div class="skill-icon text-center mx-8">
                        <div class="w-16 h-16 rounded-lg mx-auto mb-3 overflow-hidden">
                            <img src="8.png" alt="Premiere Pro" class="skill-image">
                        </div>
                        <span class="text-sm text-gray-600">300.000</span>
                    </div>

                </div>
            </div>
        </div>
        
    </section>

    <!-- Portfolio Section -->
    <section id="portfolio" class="py-20 bg-white">
        <div class="container mx-auto px-6">
            <h2 class="section-title text-4xl font-bold text-center text-gray-800 mb-16">REMAKE</h2>
            
            <!-- MEDIA Section - 세로 늘림 -->
            <div class="mb-20">
                <h3 class="text-2xl font-semibold text-gray-800 mb-8">UNIONMADE REMAKE EDI</h3>
                <div class="grid md:grid-cols-2 gap-8">
                    <div class="portfolio-item">
                        <div class="bg-gray-200 rounded-lg overflow-hidden video-thumbnail" onclick="window.open('https://fruitsfamily.com/product/42zvj/canadian-tanker-jacket-l', '_blank')">
                            <div class="h-80 relative">
                                <img src="9.jpg" alt="UNIONMADE REMAKE" class="w-full h-full object-cover">
                                <div class="absolute inset-0 bg-black bg-opacity-20 flex items-center justify-center">
                                    <div class="text-white text-center">
                                    </div>
                                </div>
                            </div>
                        </div>
                            <h4 class="media-title text-lg font-semibold mt-4 text-center">canadian tanker jacket (L)</h4>
                                <p class="text-gray-600 text-l text-center" onclick="openDetailPage('busan')">230.000</p>

                    </div>
                    <div class="portfolio-item">
                        <div class="bg-gray-200 rounded-lg overflow-hidden video-thumbnail" onclick="window.open('https://fruitsfamily.com/seller/ipjt/unionmadevintage?sort=NEW', '_blank')">
                            <div class="h-80 relative">
                                <img src="10.jpg" alt="UNIONMADE REMAKE" class="w-full h-full object-cover">
                                <div class="absolute inset-0 bg-black bg-opacity-20 flex items-center justify-center">
                                    <div class="text-white text-center">
                                    </div>
                                </div>
                            </div>
                        </div>
                            <h4 class="media-title text-lg font-semibold mt-4 text-center">UNIONMADE REMAKE ED FLYING TIGER</h4>
                                <p class="text-gray-600 text-l text-center" onclick="openDetailPage('busan')">45.000</p>
                    </div>
                    <div class="portfolio-item">
                        <div class="bg-gray-200 rounded-lg overflow-hidden video-thumbnail" onclick="window.open('https://fruitsfamily.com/seller/ipjt/unionmadevintage?sort=NEW', '_blank')">
                            <div class="h-80 relative">
                                <img src="11.jpg" alt="단편영화" class="w-full h-full object-cover">
                                <div class="absolute inset-0 bg-black bg-opacity-20 flex items-center justify-center">
                                    <div class="text-white text-center">
                                    </div>
                                </div>
                            </div>
                        </div>
                            <h4 class="media-title text-lg font-semibold mt-4 text-center">UNIONMADE REMAKE ED FLYING BEE</h4>
                                <p class="text-gray-600 text-l text-center" onclick="openDetailPage('busan')">60.000</p>
                    </div>
                    <div class="portfolio-item">
                        <div class="bg-gray-200 rounded-lg overflow-hidden video-thumbnail" onclick="window.open('https://fruitsfamily.com/seller/ipjt/unionmadevintage?sort=NEW', '_blank')">
                            <div class="h-80 relative">
                                <img src="12.jpg" alt="미디어아트" class="w-full h-full object-cover">
                                <div class="absolute inset-0 bg-black bg-opacity-20 flex items-center justify-center">
                                    <div class="text-white text-center">
                                    </div>
                                </div>
                            </div>
                        </div>
                            <h4 class="media-title text-lg font-semibold mt-4 text-center">UNIONMADE REMAKE ED MADIC</h4>
                                <p class="text-gray-600 text-l text-center" onclick="openDetailPage('busan')">45.000</p>
                    </div>
                </div>
            </div>

            <!-- BI BX Section - 크기 줄임 -->
            <div class="mb-20">
                <h3 class="text-2xl font-semibold text-gray-800 mb-8">WILL FTURE</h3>
                <div class="bi-bx-container">
                    <div class="bi-bx-slide active">
                        <img src="13.png" alt="LUXMETIC - Premium Brand Identity">
                    </div>
                    <div class="bi-bx-slide">
                        <img src="14.png" alt="Package Design - Face Cream & Bath Products">
                    </div>
                    <div class="bi-bx-slide">
                        <img src="15.png" alt="Brand Applications - Business Cards & Stationery">
                    </div>
                    <div class="bi-bx-slide">
                        <img src="13.png" alt="Marketing Materials - Posters & Advertisements">
                    </div>
                    <div class="bi-bx-slide">
                        <img src="14.png" alt="Marketing Materials - Posters & Advertisements">
                    </div>
                    <div class="bi-bx-slide">
                        <img src="15.png" alt="Marketing Materials - Posters & Advertisements">
                    </div>
                    <div class="bi-bx-slide">
                        <img src="13.png" alt="Marketing Materials - Posters & Advertisements">
                    </div>
                    <div class="bi-bx-slide">
                        <img src="14.png" alt="Marketing Materials - Posters & Advertisements">
                    </div>
                    <div class="bi-bx-slide">
                        <img src="15.png" alt="Marketing Materials - Posters & Advertisements">
                    </div>
                </div>
            </div>




    <!-- Contact Section -->
    <section id="contact" class="py-20 bg-black text-white">
        <div class="container mx-auto px-8 text-center">
            <h2 class="text-4xl font-bold mb-8">CONTACT UNIONMADE</h2>
            <p class="text-xl mb-12 opacity-90">“저희는 경험을 공유합니다.<br>
                                                앞으로도 실험을 두려워하지 않고,<br>
                                                더 나은 브랜드를 만들기 위해 성장하겠습니다.”</p>
            <div class="flex justify-center space-x-8 mb-12">
                <a href="mailto:parkeunji8440@naver.com" class="flex items-center space-x-2 hover:opacity-80 transition-opacity">
                    <i class="fas fa-envelope text-xl"></i>
                    <span>UNIONMADE_VTG_instagram</span>
                </a>
                <a href="tel:+82-10-1234-5678" class="flex items-center space-x-2 hover:opacity-80 transition-opacity">
                    <i class="fas fa-phone text-2xl"></i>
                    <span>010-2428-7461</span>
                </a>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="bg-gray-800 text-white py-8">
        <div class="container mx-auto px-6 text-center">
            <p>&copy; 2025 unionmade vtg.</p>
        </div>
    </footer>

    <script>
        // Smooth scrolling for navigation links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });

        // Add scroll effect to navigationㄹ
        window.addEventListener('scroll', function() {
            const nav = document.querySelector('nav');
            if (window.scrollY > 50) {
                nav.classList.add('bg-white');
                nav.classList.remove('bg-opacity-80');
                nav.classList.add('bg-opacity-95');
            } else {
                nav.classList.remove('bg-opacity-95');
                nav.classList.add('bg-opacity-80');
            }
        });

        // BI BX slideshow
        let currentSlide = 0;
        const slides = document.querySelectorAll('.bi-bx-slide');
        
        function showNextSlide() {
            slides[currentSlide].classList.remove('active');
            currentSlide = (currentSlide + 1) % slides.length;
            slides[currentSlide].classList.add('active');
        }
        
        setInterval(showNextSlide, 2000);

</script>
</body>
</html>
