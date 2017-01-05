var nude_image = "EMINNUDE1.jpeg";
var sorbet_image = "EMINSORBET1.jpeg";
var nude = '<div class="item active"><img id="emin-one" class="img-responsive" src="/static/images/EMINNUDE1.jpeg" alt=""></div><div class="item"><img id="emin-two" class="img-responsive" src="/static/images/EMINNUDE2.jpeg" alt=""></div><div class="item"><img id="emin-three" class="img-responsive" src="/static/images/EMINNUDE3.jpg" alt=""></div><div class="item"><img id="emin-four" class="img-responsive" src="/static/images/EMINNUDE4.jpeg" alt=""></div>'
var sorbet = '<div class="item active"><img id="emin-five" class="img-responsive" src="/static/images/EMINSORBET1.jpeg" alt="..."></div><div class="item"><img id="emin-six" class="img-responsive" src="/static/images/EMINSORBET2.jpeg" alt="..."></div><div class="item"><img id="emin-seven" class="img-responsive" src="/static/images/EMINSORBET3.jpeg" alt="..."></div><div class="item"><img id="emin-eight" class="img-responsive" src="/static/images/EMINSORBET4.jpeg" alt="..."></div>'

function onChange() {
	// get selected option
	var item_colour = document.getElementById("item-colour");
	var selected_colour = item_colour.options[item_colour.selectedIndex].textContent;

	// if NUDE or SORBET, update to relevant 

	if (selected_colour == "NUDE") {
		document.getElementById("emin").src = "/static/images/" + nude_image;
		document.getElementsByClassName("carousel-inner")[0].innerHTML = nude;
	}

	if (selected_colour == "SORBET") {
		document.getElementById("emin").src = "/static/images/" + sorbet_image;
		document.getElementsByClassName("carousel-inner")[0].innerHTML = sorbet;
	}
}