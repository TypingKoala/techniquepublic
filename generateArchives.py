header = """
<!DOCTYPE html>
<html>

<head>
  <meta http-equiv="content-type" content="text/html;charset=UTF-8" />
  <meta charset="utf-8" />
  <title>Technique</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
  <link rel="apple-touch-icon" href="pages/ico/60.png">
  <link rel="apple-touch-icon" sizes="76x76" href="pages/ico/76.png">
  <link rel="apple-touch-icon" sizes="120x120" href="pages/ico/120.png">
  <link rel="apple-touch-icon" sizes="152x152" href="pages/ico/152.png">
  <link rel="icon" type="image/x-icon" href="favicon.ico" />
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-touch-fullscreen" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="default">
  <meta content="" name="description" />
  <meta content="" name="author" />
  <!-- BEGIN PLUGINS -->
  <link href="assets/plugins/pace/pace-theme-flash.css" rel="stylesheet" type="text/css" />
  <link href="assets/plugins/bootstrap/css/bootstrap.min.css" rel="stylesheet" type="text/css" />
  <link href="assets/plugins/font-awesome/css/all.css" rel="stylesheet" type="text/css" />
  <link href="assets/plugins/swiper/css/swiper.css" rel="stylesheet" type="text/css" media="screen" />
  <link href="https://fonts.googleapis.com/css?family=Raleway:600&display=swap" rel="stylesheet">

  <!-- END PLUGINS -->
  <!-- BEGIN PAGES CSS -->
  <link class="main-stylesheet" href="pages/css/pages.css" rel="stylesheet" type="text/css" />
  <link href="pages/css/pages-icons.css" rel="stylesheet" type="text/css" />
  <!-- BEGIN PAGES CSS -->
</head>

<body class="pace-white">
  <!-- BEGIN HEADER -->
  <nav class="header bg-header minimized dark " data-pages="header">
    <div class="container relative">
      <!-- BEGIN LEFT CONTENT -->
      <div class="pull-left">
        <!-- .header-inner Allows to vertically Align elements to the Center-->
        <div class="header-inner"
          style="color: white; font-size: 20px; font-weight: bold; font-family: 'Raleway', sans-serif;">
          <!-- BEGIN LOGO -->
          TECHNIQUE
        </div>
      </div>
      <!-- BEGIN HEADER TOGGLE FOR MOBILE & TABLET -->
      <div class="pull-right">
        <div class="header-inner">
          <div class="visible-sm-inline visible-xs-inline menu-toggler pull-right p-l-10" data-pages="header-toggle"
            data-pages-element="#header">
            <div class="one"></div>
            <div class="two"></div>
            <div class="three"></div>
          </div>
        </div>
      </div>
      <!-- END HEADER TOGGLE FOR MOBILE & TABLET -->
      <!-- BEGIN RIGHT CONTENT -->
      <div class="pull-right menu-content mobile-dark clearfix" data-pages="menu-content"
        data-pages-direction="slideRight" id="header">
        <!-- BEGIN HEADER CLOSE TOGGLE FOR MOBILE -->
        <div class="pull-right">
          <a href="#" class="padding-10 visible-xs-inline visible-sm-inline pull-right m-t-10 m-b-10 m-r-10"
            data-pages="header-toggle" data-pages-element="#header">
            <i class=" pg-close_line"></i>
          </a>
        </div>
        <!-- END HEADER CLOSE TOGGLE FOR MOBILE -->
        <!-- BEGIN MENU ITEMS -->
        <div class="header-inner">
          <ul class="menu">
            <li>
              <a href="index.html" data-text="Home">Home </a>
            </li>
            <li>
              <a href="about.html" data-text="About" class="active">About </a>
            </li>
            <li>
              <a href="seniors.html" data-text="Seniors">Seniors </a>
            </li>
            <li>
              <a href="order.html" data-text="Order">Order </a>
            </li>
            <li>
              <a href="hire.html" data-text="Hire Us">Hire Us </a>
            </li>
            <li>
              <a href="contact.html" data-text="Contact" class="b-r b-transparent-white">Contact </a>
            </li>
            <li>
              <a class="email-btn" data-clipboard-text="technique@mit.edu" style="cursor: pointer">technique@mit.edu</a>
            </li>
          </ul>
        </div>
        <!-- END MENU ITEMS -->
      </div>
    </div>
  </nav>
  <div class="p-t-60">
    <!-- END HEADER -->
    <!-- BEGIN INTRO CONTENT -->
    <section class="p-b-20 p-t-70">
      <div class="container text-center">
        <div class="row">
          <div class="col-sm-8 col-sm-offset-2">
            <h1 class="m-t-5 light">Archives</h1>
            <p>Take a look at some past editions of Technique.</p>
          </div>

        </div>
      </div>
    </section>
    <!-- END INTRO CONTENT -->
    <!-- START CONTENT SECTION -->
    <section class="p-b-60">
      <div class="container">
        <div class="row">
          <div class="col-sm-8 col-sm-offset-2">
            <div class="m-t-20">
              <section>
                <div class="row">
"""
footer = """
                </div>
              </section>
            </div>
          </div>
        </div>
      </div>
    </section>
    <!-- END CONTENT SECTION -->
    <!-- BEGIN FOOTER -->
    <section class="p-b-50 p-t-50 bg-master-darker ">
      <div class="container">
        <div class="row">
          <div class="col-md-12">
            <p class="fs-11 no-margin font-arial text-white small-text">
            </p>
            <p class="fs-11 hint-text text-white font-arial no-margin small-text">Web content © 2019 Technique. Images
              are
              property of their respective owners. All Rights Reserved.</p>
            <ul class="no-style fs-11 no-padding font-arial m-t-20">
            </ul>
          </div>
        </div>
      </div>
    </section>
    <!-- END FOOTER -->
    <!-- BEGIN CORE FRAMEWORK -->
    <script src="assets/plugins/pace/pace.min.js" type="text/javascript"></script>
    <script type="text/javascript" src="pages/js/pages.image.loader.js"></script>
    <script type="text/javascript" src="assets/plugins/jquery/jquery-1.11.1.min.js"></script>
    <script type="text/javascript" src="assets/plugins/bootstrap/js/bootstrap.min.js"></script>
    <script type="text/javascript" src="assets/plugins/clipboard/clipboard.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/typed.js@2.0.9"></script>
    <script type="text/javascript" src="assets/plugins/popper/popper.min.js"></script>
    <script type="text/javascript" src="assets/plugins/tippy/tippy.min.js"></script>>
    <!-- BEGIN SWIPER DEPENDENCIES -->
    <script type="text/javascript" src="assets/plugins/swiper/js/swiper.jquery.min.js"></script>
    <script type="text/javascript" src="assets/plugins/jquery-validation/js/jquery.validate.min.js"></script>
    <script src="https://maps.googleapis.com/maps/api/js?v=3.exp"></script>
    <!-- BEGIN RETINA IMAGE LOADER -->
    <script type="text/javascript" src="assets/plugins/jquery-unveil/jquery.unveil.min.js"></script>
    <!-- END VENDOR JS -->
    <!-- BEGIN PAGES FRONTEND LIB -->
    <script type="text/javascript" src="pages/js/pages.frontend.js"></script>
    <!-- END PAGES LIB -->
    <!-- BEGIN YOUR CUSTOM JS -->
    <script type="text/javascript" src="assets/js/custom.js"></script>
    <script type="text/javascript" src="assets/js/contact.js"></script>
    <script type="text/javascript" src="assets/js/google_map.js"></script>
</body>

</html>
"""

class Yearbook:
    def __init__(self, title, filename, thumbnail):
        self.title = title
        self.filename = filename
        self.thumbnail = thumbnail

books = []

def addRegularBook(year):
    books.append(
        Yearbook(
            "Technique {}".format(year),
            "http://web.mit.edu/technique/www/scans/{}_Technique.pdf".format(year),
            "/assets/images/covers/{}_Technique@2x.jpg".format(year)
        )
    )

for year in range(1885, 1917):
    if year not in [1888, 1891]:
        addRegularBook(year)

books.append(
    Yearbook(
        "New Campus Sketches 1916",
        "http://web.mit.edu/technique/www/scans/1916_MIT_Sketches.pdf",
        "/assets/images/covers/1916_MIT_Sketches@2x.jpg"
    )
)

for year in range(1917, 1920):
    addRegularBook(year)

books.append(
    Yearbook(
        "War Record 1919",
        "http://web.mit.edu/technique/www/scans/1919_War_Record.pdf",
        "/assets/images/covers/1919_War_Record@2x.jpg"
    )
)

for year in range(1920, 1924):
    addRegularBook(year)

books.append(
    Yearbook(
        "Technique 1924 (Vol 38)",
        "http://web.mit.edu/technique/www/scans/1924_Technique_Vol38.pdf",
        "/assets/images/covers/1924_Technique_Vol38@2x.jpg"
    )
)
books.append(
    Yearbook(
        "Technique 1924 (Vol 39)",
        "http://web.mit.edu/technique/www/scans/1924_Technique_Vol39.pdf",
        "/assets/images/covers/1924_Technique_Vol39@2x.jpg"
    )
)

for year in range(1925, 1929):
    addRegularBook(year)

books.append(
    Yearbook(
        "Freshman Gray Book",
        "http://web.mit.edu/technique/www/scans/1928_Freshman_Gray_Book.pdf",
        "/assets/images/covers/1928_Freshman_Gray_Book@2x.jpg"
    )
)

for year in range(1929, 1931):
    addRegularBook(year)

with open("archives.html", "w") as f:
    f.write(header)
    for yearbook in books:
        replace = {
            "filename": yearbook.filename,
            "thumbnail": yearbook.thumbnail,
            "title": yearbook.title
        }
        entry = """
                  <div class="col-md-4 p-b-20">
                    <figure class="figure">
                        <a class="cover" target="_blank" href="{filename}">
                          <img src="{thumbnail}" alt="{title} Cover" width="220" height="293">
                          <figcaption class="figure-caption">{title}</figcaption>
                        </a>
                    </figure>
                  </div>
""".format(**replace)
        f.write(entry)
    f.write(footer)