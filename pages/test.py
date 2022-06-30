import streamlit as st
import streamlit.components.v1 as components

# bootstrap 4 collapse example
components.html("""
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>
<style>
/* Custom style to prevent carousel from being distorted 
   if for some reason image doesn't load */
.carousel-item{
    min-height: 280px;
}
</style>
</head>
<body>
<div class="container-lg my-3">
    <div id="myCarousel" class="carousel slide" data-bs-ride="carousel">
        <!-- Carousel indicators -->
        <ol class="carousel-indicators">
            <li data-bs-target="#myCarousel" data-bs-slide-to="0" class="active"></li>
            <li data-bs-target="#myCarousel" data-bs-slide-to="1"></li>
            <li data-bs-target="#myCarousel" data-bs-slide-to="2"></li>
        </ol>
        
        <!-- Wrapper for carousel items -->
        <div class="carousel-inner">
            <div class="carousel-item active">
                <img src="/examples/images/slide1.png" class="d-block w-100" alt="Slide 1">
                <div class="carousel-caption d-none d-md-block">
                    <h5>First slide label</h5>
                    <p>Some demonstrative placeholder content for the first slide.</p>
                </div>
            </div>
            <div class="carousel-item">
                <img src="/examples/images/slide2.png" class="d-block w-100" alt="Slide 2">
                <div class="carousel-caption d-none d-md-block">
                    <h5>Second slide label</h5>
                    <p>Some demonstrative placeholder content for the second slide.</p>
                </div>
            </div>
            <div class="carousel-item">
                <img src="/examples/images/slide3.png" class="d-block w-100" alt="Slide 3">
                <div class="carousel-caption d-none d-md-block">
                    <h5>Third slide label</h5>
                    <p>Some demonstrative placeholder content for the third slide.</p>
                </div>
            </div>
        </div>

        <!-- Carousel controls -->
        <a class="carousel-control-prev" href="#myCarousel" data-bs-slide="prev">
            <span class="carousel-control-prev-icon"></span>
        </a>
        <a class="carousel-control-next" href="#myCarousel" data-bs-slide="next">
            <span class="carousel-control-next-icon"></span>
        </a>
    </div>
    
    <div class="alert alert-info mt-3">
        Carousel caption will be hidden on smaller viewport, but become visible on medium devices (i.e. viewport width &ge;768px). Change orientation of this HTML editor to see how it works. 
    </div>
</div>

    """,
    height=800,
)