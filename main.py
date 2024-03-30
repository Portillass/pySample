from flask import Flask, render_template_string

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Landing Page</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
</head>
<body>
    <header>
        <div class="container">
            <nav>
                <div class="logo">
                    <a href="/">JP</a>
                </div>
                <ul class="menu">
                    <li><a href="#home"><i class="fas fa-home"></i> Home</a></li>
                    <li><a href="#about"><i class="fas fa-user"></i> About</a></li>
                    <li><a href="#goals"><i class="fas fa-bullseye"></i> Goals</a></li>
                    <li><a href="#family"><i class="fas fa-users"></i> Family</a></li>
                    <li><a href="#loved-ones"><i class="fas fa-heart"></i> My Loved Ones</a></li>
                    <li><a href="#contact"><i class="fas fa-envelope"></i> Contact</a></li>
                </ul>
                <div class="menu-toggle">
                    <i class="fas fa-bars"></i>
                </div>
            </nav>
        </div>
    </header>



    <!-- Home Section -->
    <section id="home">
        <div class="container">
            <div class="home-content">
                <h1>Hi, I'm <span>JARELL E. PORTILLAS</span></h1>
                <p>A passionate developer dedicated to creating exceptional digital experiences</p>
                <div class="home-btn-group">
                    <a href="#about" class="btn">Learn More</a>
                    <a href="#contact" class="btn" style="background-color: transparent; border: 2px solid #fff;">Contact Me</a>
                </div>
            </div>
        </div>
    </section>

    <!-- About Section -->
    <section id="about">
        <div class="container">
            <div class="section-title">
                <h2>About Me</h2>
            </div>
            <div class="about-content">
                <div class="about-img">
                    <img src="{{ url_for('static', filename='images/profile.jpg') }}" alt="Jarell E. Portillas">
                </div>
                <div class="about-text">
                    <h3>A Passionate Developer</h3>
                    <p>Hello! I'm Jarell E. Portillas, a passionate developer from Bukidnon State University. My journey in development started with a curiosity about how websites work and has evolved into a professional career.</p>
                    <p>I specialize in full-stack development using modern technologies and frameworks. I'm constantly learning and improving my skills to deliver the best possible solutions.</p>
                    <div class="skills">
                        <div class="skill-item">
                            <div class="skill-name">
                                <span>HTML/CSS</span>
                                <span>95%</span>
                            </div>
                            <div class="skill-bar">
                                <div class="skill-progress" style="width: 95%"></div>
                            </div>
                        </div>
                        <div class="skill-item">
                            <div class="skill-name">
                                <span>JavaScript</span>
                                <span>90%</span>
                            </div>
                            <div class="skill-bar">
                                <div class="skill-progress" style="width: 90%"></div>
                            </div>
                        </div>
                        <div class="skill-item">
                            <div class="skill-name">
                                <span>React</span>
                                <span>85%</span>
                            </div>
                            <div class="skill-bar">
                                <div class="skill-progress" style="width: 85%"></div>
                            </div>
                        </div>
                        <div class="skill-item">
                            <div class="skill-name">
                                <span>Python</span>
                                <span>80%</span>
                            </div>
                            <div class="skill-bar">
                                <div class="skill-progress" style="width: 80%"></div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Goals Section -->
    <section id="goals">
        <div class="container">
            <div class="section-title">
                <h2>My Goals</h2>
            </div>
            <div class="goals-container">
                <div class="goal-item">
                    <div class="goal-icon">
                        <i class="fas fa-smile"></i>
                    </div>
                    <h3 class="goal-title">Find Happiness</h3>
                    <p class="goal-text">My main goal in life is to be happy and to share that happiness with my loved ones.</p>
                </div>
                <div class="goal-item">
                    <div class="goal-icon">
                        <i class="fas fa-laptop-code"></i>
                    </div>
                    <h3 class="goal-title">Technical Mastery</h3>
                    <p class="goal-text">Master advanced web development techniques and stay current with the latest technologies and frameworks.</p>
                </div>
                <div class="goal-item">
                    <div class="goal-icon">
                        <i class="fas fa-project-diagram"></i>
                    </div>
                    <h3 class="goal-title">Build a Portfolio</h3>
                    <p class="goal-text">Create a diverse portfolio of impactful projects that demonstrate my skills and creativity.</p>
                </div>
                <div class="goal-item">
                    <div class="goal-icon">
                        <i class="fas fa-code-branch"></i>
                    </div>
                    <h3 class="goal-title">Open Source</h3>
                    <p class="goal-text">Actively contribute to open-source communities and collaborate with developers worldwide.</p>
                </div>
                <div class="goal-item">
                    <div class="goal-icon">
                        <i class="fas fa-users"></i>
                    </div>
                    <h3 class="goal-title">Mentorship</h3>
                    <p class="goal-text">Mentor junior developers and share knowledge to help others grow in their careers.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Family Section -->
    <section id="family">
        <div class="container">
            <div class="section-title">
                <h2>My Family</h2>
            </div>
            <div class="family-content">
                <div class="family-text">
                    <h3>The People Who Inspire Me</h3>
                    <p>I'm blessed to have a supportive family that has always been there for me through my journey:</p>
                    <ul class="family-list">
                        <li><strong>Janeth Portillas</strong> - My loving mother who has always believed in me</li>
                        <li><strong>Ruel Portillas</strong> - My father who taught me the value of hard work</li>
                        <li><strong>My Two Sisters</strong> - Who have been my companions and supporters</li>
                    </ul>
                    <p>Special mention to <strong>Lea</strong>, who holds a special place in my heart.</p>
                </div>
                <div class="family-slideshow">
                    <div class="family-slide active">
                        <img src="{{ url_for('static', filename='images/loved2.jpeg') }}" alt="Family Member 1">
                        <div class="slide-info">
                            <h4>Janeth Portillas</h4>
                            <p>My loving mother who has always been my biggest supporter and guide through life.</p>
                        </div>
                    </div>
                    <div class="family-slide">
                        <img src="{{ url_for('static', filename='images/loved4.jpg') }}" alt="Family Member 2">
                        <div class="slide-info">
                            <h4>Ruel Portillas</h4>
                            <p>My father who taught me the value of hard work and perseverance.</p>
                        </div>
                    </div>
                    <div class="family-slide">
                        <img src="{{ url_for('static', filename='images/loved5.jpg') }}" alt="Family Member 3">
                        <div class="slide-info">
                            <h4>My Sisters</h4>
                            <p>My wonderful sisters who have been my companions and supporters throughout life.</p>
                        </div>
                    </div>
                    <div class="family-slide">
                        <img src="{{ url_for('static', filename='images/loved1.jpeg') }}" alt="Family Member 4">
                        <div class="slide-info">
                            <h4>Lea</h4>
                            <p>The special someone who holds a unique place in my heart.</p>
                        </div>
                    </div>
                    <div class="slide-navigation">
                        <span class="prev-slide"><i class="fas fa-chevron-left"></i></span>
                        <span class="next-slide"><i class="fas fa-chevron-right"></i></span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- My Loved Ones Section -->
    <section id="loved-ones">
        <div class="container">
            <div class="section-title">
                <h2>My Loved Ones</h2>
            </div>
            <div class="loved-ones-content">
                <div class="loved-ones-text">
                    <h3>Special People in My Life</h3>
                    <p>These are the special people who make my life complete:</p>
                    <ul class="loved-ones-list">
                        <li>
                            <div class="loved-ones-item">
                                <div class="loved-ones-icon">
                                    <i class="fas fa-heart"></i>
                                </div>
                                <div class="loved-ones-info">
                                    <strong>Lea</strong>
                                    <p>My special someone who brings joy to my life</p>
                                </div>
                            </div>
                        </li>
                        <li>
                            <div class="loved-ones-item">
                                <div class="loved-ones-icon">
                                    <i class="fas fa-users"></i>
                                </div>
                                <div class="loved-ones-info">
                                    <strong>My Best Friends</strong>
                                    <p>Who have been there through thick and thin</p>
                                </div>
                            </div>
                        </li>
                        <li>
                            <div class="loved-ones-item">
                                <div class="loved-ones-icon">
                                    <i class="fas fa-home"></i>
                                </div>
                                <div class="loved-ones-info">
                                    <strong>My Extended Family</strong>
                                    <p>Who provide endless support and love</p>
                                </div>
                            </div>
                        </li>
                    </ul>
                </div>
                <div class="loved-ones-slideshow">
                    <div class="loved-ones-slide active">
                        <img src="{{ url_for('static', filename='images/loved1.jpeg') }}" alt="Loved One 1">
                        <div class="slide-info">
                            <h4>Lea</h4>
                            <p>My special someone who brings joy and happiness to my life every day.</p>
                        </div>
                    </div>
                    <div class="loved-ones-slide">
                        <img src="{{ url_for('static', filename='images/loved6.jpg') }}" alt="Loved One 2">
                        <div class="slide-info">
                            <h4>Best Friends</h4>
                            <p>My best friends who have stood by me through all life's challenges.</p>
                        </div>
                    </div>
                    <div class="loved-ones-slide">
                        <img src="{{ url_for('static', filename='images/loved7.jpg') }}" alt="Loved One 3">
                        <div class="slide-info">
                            <h4>Extended Family</h4>
                            <p>My extended family who provide unconditional love and support.</p>
                        </div>
                    </div>
                    <div class="loved-ones-slide">
                        <img src="{{ url_for('static', filename='images/loved8.jpg') }}" alt="Loved One 4">
                        <div class="slide-info">
                            <h4>Special Moments</h4>
                            <p>Precious memories with all the special people in my life.</p>
                        </div>
                    </div>
                    <div class="slide-navigation">
                        <span class="prev-slide"><i class="fas fa-chevron-left"></i></span>
                        <span class="next-slide"><i class="fas fa-chevron-right"></i></span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact">
        <div class="container">
            <div class="section-title">
                <h2>Contact Me</h2>
            </div>
            <div class="contact-content">
                <div class="contact-info">
                    <div class="contact-item">
                        <div class="icon"><i class="fas fa-envelope"></i></div>
                        <div class="text">
                            <h3>Email</h3>
                            <p>portillasjep@gmail.com</p>
                        </div>
                    </div>
                    <div class="contact-item">
                        <div class="icon"><i class="fas fa-phone"></i></div>
                        <div class="text">
                            <h3>Phone</h3>
                            <p>+63 123 456 7890</p>
                        </div>
                    </div>
                    <div class="contact-item">
                        <div class="icon"><i class="fas fa-map-marker-alt"></i></div>
                        <div class="text">
                            <h3>Location</h3>
                            <p>Bukidnon, Philippines</p>
                        </div>
                    </div>
                    <div class="social-links">
                        <a href="https://github.com/portillass" target="_blank"><i class="fab fa-github"></i></a>
                        <a href="https://www.facebook.com/jarell.portillas.2024" target="_blank"><i class="fab fa-facebook"></i></a>
                        <a href="https://linkedin.com/in/jarellportillas" target="_blank"><i class="fab fa-linkedin"></i></a>
                        <a href="https://twitter.com/jarellportillas" target="_blank"><i class="fab fa-twitter"></i></a>
                    </div>
                </div>
                <div class="contact-form">
                    <form>
                        <div class="form-group">
                            <input type="text" name="name" placeholder="Your Name" required>
                        </div>
                        <div class="form-group">
                            <input type="email" name="email" placeholder="Your Email" required>
                        </div>
                        <div class="form-group">
                            <input type="text" name="subject" placeholder="Subject" required>
                        </div>
                        <div class="form-group">
                            <textarea name="message" placeholder="Your Message" required></textarea>
                        </div>
                        <button type="submit" class="btn">Send Message</button>
                    </form>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <div class="container">
            <div class="footer-logo">
                <img src="static/images/logo.png" alt="Logo" style="height: 50px; width: auto;">
            </div>
            <div class="social-links">
                <a href="#"><i class="fab fa-facebook-f"></i></a>
                <a href="#"><i class="fab fa-twitter"></i></a>
                <a href="#"><i class="fab fa-instagram"></i></a>
                <a href="#"><i class="fab fa-linkedin-in"></i></a>
            </div>
            <div class="copyright">
                &copy; 2025 My Portfolio. Develop By Rell.
            </div>
        </div>
    </footer>

    <!-- Back to top button -->
    <a href="#" class="back-to-top">
        <i class="fas fa-arrow-up"></i>
    </a>

    <!-- JavaScript -->
    <script>
        // Mobile Menu Toggle
        const menuToggle = document.querySelector('.menu-toggle');
        const menu = document.querySelector('.menu');
        
        menuToggle.addEventListener('click', () => {
            menu.classList.toggle('active');
            menuToggle.classList.toggle('active');
        });
        
        // Smooth Scrolling
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                
                if (menu.classList.contains('active')) {
                    menu.classList.remove('active');
                    menuToggle.classList.remove('active');
                }
                
                document.querySelector(this.getAttribute('href')).scrollIntoView({
                    behavior: 'smooth'
                });
            });
        });
        
        // Slideshow functionality
        function initSlideshow(containerClass, slideClass) {
            const slideshow = document.querySelector(`.${containerClass}`);
            if (!slideshow) return;
            
            const slides = slideshow.querySelectorAll(`.${slideClass}`);
            const prevBtn = slideshow.querySelector('.prev-slide');
            const nextBtn = slideshow.querySelector('.next-slide');
            let currentSlide = 0;
            let slideInterval;
            
            function showSlide(index) {
                // Hide all slides
                slides.forEach(slide => {
                    slide.classList.remove('active');
                });
                
                // Show current slide
                slides[index].classList.add('active');
            }
            
            function nextSlide() {
                currentSlide = (currentSlide + 1) % slides.length;
                showSlide(currentSlide);
            }
            
            function prevSlide() {
                currentSlide = (currentSlide - 1 + slides.length) % slides.length;
                showSlide(currentSlide);
            }
            
            // Set up automatic slideshow
            function startSlideshow() {
                slideInterval = setInterval(nextSlide, 5000);
            }
            
            function stopSlideshow() {
                clearInterval(slideInterval);
            }
            
            // Event listeners for navigation buttons
            if (prevBtn) {
                prevBtn.addEventListener('click', () => {
                    prevSlide();
                    stopSlideshow();
                    startSlideshow();
                });
            }
            
            if (nextBtn) {
                nextBtn.addEventListener('click', () => {
                    nextSlide();
                    stopSlideshow();
                    startSlideshow();
                });
            }
            
            // Pause on hover
            slideshow.addEventListener('mouseenter', stopSlideshow);
            slideshow.addEventListener('mouseleave', startSlideshow);
            
            // Start slideshow
            showSlide(0);
            startSlideshow();
        }
        
        // Initialize slideshows when page content is loaded
        document.addEventListener('DOMContentLoaded', function() {
            initSlideshow('family-slideshow', 'family-slide');
            initSlideshow('loved-ones-slideshow', 'loved-ones-slide');
        });
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_PAGE)

@app.route('/portfolio')
def portfolio():
    return render_template_string(PORTFOLIO_PAGE)

if __name__ == '__main__':
    app.run(debug=True)
