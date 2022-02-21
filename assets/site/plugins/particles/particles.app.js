/* -----------------------------------------------
/* How to use? : Check the GitHub README
/* ----------------------------------------------- */

/* To load a config file (particles.json) you need to host this demo (MAMP/WAMP/local)... */
/*
particlesJS.load('particles-js', 'particles.json', function() {
  console.log('particles.js loaded - callback');
});
*/

/* Otherwise just put the config content (json): */
(function($){


if($('#particles-js').length > 0 )
{
	particlesJS('particles-js',
	  {
	  "particles": {
		"number": {
		  "value": 80,
		  "density": {
			"enable": true,
			"value_area": 800
		  }
		},
		"color": {
		  "value": "#ffffff"
		},
		"shape": {
		  "type": "circle",
		  "stroke": {
			"width": 0,
			"color": "#000000"
		  },
		  "polygon": {
			"nb_sides": 5
		  },
		  "image": {
			"src": "img/github.svg",
			"width": 100,
			"height": 100
		  }
		},
		"opacity": {
		  "value": 0.616754040155689,
		  "random": false,
		  "anim": {
			"enable": false,
			"speed": 1,
			"opacity_min": 0.1,
			"sync": false
		  }
		},
		"size": {
		  "value": 3,
		  "random": true,
		  "anim": {
			"enable": false,
			"speed": 40,
			"size_min": 0.1,
			"sync": false
		  }
		},
		"line_linked": {
		  "enable": true,
		  "distance": 120,
		  "color": "#ffffff",
		  "opacity": 0.6000850120433731,
		  "width": 1
		},
		"move": {
		  "enable": true,
		  "speed": 1.2,
		  "direction": "none",
		  "random": true,
		  "straight": false,
		  "out_mode": "bounce",
		  "bounce": false,
		  "attract": {
			"enable": true,
			"rotateX": 315.6640387635437,
			"rotateY": 946.9921162906311
		  }
		}
	  },
	  "interactivity": {
		"detect_on": "canvas",
		"events": {
		  "onhover": {
			"enable": false,
			"mode": "grab"
		  },
		  "onclick": {
			"enable": false,
			"mode": "push"
		  },
		  "resize": true
		},
		"modes": {
		  "grab": {
			"distance": 400,
			"line_linked": {
			  "opacity": 1
			}
		  },
		  "bubble": {
			"distance": 400,
			"size": 40,
			"duration": 2,
			"opacity": 8,
			"speed": 3
		  },
		  "repulse": {
			"distance": 200,
			"duration": 0.4
		  },
		  "push": {
			"particles_nb": 4
		  },
		  "remove": {
			"particles_nb": 2
		  }
		}
	  },
	  "retina_detect": true
	}

	);
	
}

if($('#particles-star').length > 0 )
{
	particlesJS('particles-star',
	  {
	  "particles": {
		"number": {
		  "value": 100,
		  "density": {
			"enable": false,
			"value_area": 800
		  }
		},
		"color": {
		  "value": "#ffffff"
		},
		"shape": {
		  "type": "star",
		  "stroke": {
			"width": 0,
			"color": "#000000"
		  },
		  "polygon": {
			"nb_sides": 5
		  },
		  "image": {
			"src": "http://wiki.lexisnexis.com/academic/images/cargo/f/fb/Itunes_podcast_icon_300.jpg",
			"width": 100,
			"height": 100
		  }
		},
		"opacity": {
		  "value": 0.5,
		  "random": false,
		  "anim": {
			"enable": false,
			"speed": 1,
			"opacity_min": 0.1,
			"sync": false
		  }
		},
		"size": {
		  "value": 4.16725702807898,
		  "random": true,
		  "anim": {
			"enable": false,
			"speed": 5.067567567567564,
			"size_min": 14.358108108108098,
			"sync": false
		  }
		},
		"line_linked": {
		  "enable": false,
		  "distance": 16.66902811231592,
		  "color": "#ffffff",
		  "opacity": 0.1416867389546853,
		  "width": 1.5002125301084326
		},
		"move": {
		  "enable": true,
		  "speed": 1.666902811231592,
		  "direction": "none",
		  "random": true,
		  "straight": false,
		  "out_mode": "bounce",
		  "bounce": false,
		  "attract": {
			"enable": false,
			"rotateX": 7834.443212788482,
			"rotateY": 7834.443212788482
		  }
		}
	  },
	  "interactivity": {
		"detect_on": "canvas",
		"events": {
		  "onhover": {
			"enable": false,
			"mode": "grab"
		  },
		  "onclick": {
			"enable": true,
			"mode": "repulse"
		  },
		  "resize": true
		},
		"modes": {
		  "grab": {
			"distance": 200,
			"line_linked": {
			  "opacity": 1
			}
		  },
		  "bubble": {
			"distance": 400,
			"size": 40,
			"duration": 2,
			"opacity": 8,
			"speed": 3
		  },
		  "repulse": {
			"distance": 200,
			"duration": 0.4
		  },
		  "push": {
			"particles_nb": 4
		  },
		  "remove": {
			"particles_nb": 2
		  }
		}
	  },
	  "retina_detect": true
	}

	);
}	
	

if($('#particles-snow').length > 0 )
{
	particlesJS('particles-snow',
	  {
	  "particles": {
		"number": {
		  "value": 160,
		  "density": {
			"enable": true,
			"value_area": 800
		  }
		},
		"color": {
		  "value": "#ffffff"
		},
		"shape": {
		  "type": "circle",
		  "stroke": {
			"width": 0,
			"color": "#000000"
		  },
		  "polygon": {
			"nb_sides": 5
		  },
		  "image": {
			"src": "img/github.svg",
			"width": 100,
			"height": 100
		  }
		},
		"opacity": {
		  "value": 1,
		  "random": true,
		  "anim": {
			"enable": true,
			"speed": 1,
			"opacity_min": 0,
			"sync": false
		  }
		},
		"size": {
		  "value": 6,
		  "random": true,
		  "anim": {
			"enable": false,
			"speed": 4,
			"size_min": 0.3,
			"sync": false
		  }
		},
		"line_linked": {
		  "enable": false,
		  "distance": 150,
		  "color": "#ffffff",
		  "opacity": 0.4,
		  "width": 1
		},
		"move": {
		  "enable": true,
		  "speed": 1,
		  "direction": "none",
		  "random": true,
		  "straight": false,
		  "out_mode": "out",
		  "bounce": false,
		  "attract": {
			"enable": false,
			"rotateX": 600,
			"rotateY": 600
		  }
		}
	  },
	  "interactivity": {
		"detect_on": "canvas",
		"events": {
		  "onhover": {
			"enable": true,
			"mode": "bubble"
		  },
		  "onclick": {
			"enable": true,
			"mode": "repulse"
		  },
		  "resize": true
		},
		"modes": {
		  "grab": {
			"distance": 400,
			"line_linked": {
			  "opacity": 1
			}
		  },
		  "bubble": {
			"distance": 250,
			"size": 0,
			"duration": 2,
			"opacity": 0,
			"speed": 3
		  },
		  "repulse": {
			"distance": 400,
			"duration": 0.4
		  },
		  "push": {
			"particles_nb": 4
		  },
		  "remove": {
			"particles_nb": 2
		  }
		}
	  },
	  "retina_detect": true
	}
	);

}	
	
})(jQuery);