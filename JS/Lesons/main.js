$("div[class=beatmapsets__item]").hide().slideDown(2000);
$("div[class$=osu-page--beatmapsets-search-header]").hide().slideDown(1000);

let item = $("div[class=js-react--beatmaps]");
item.css("transform", "translateX(-400px)");
$("div[class=header-v4__bg-container]").css("transform", "translateX(400px)");
$("div[class=sticky-header__body]").css("transform", "translateX(700px)").css("width", "700px");
$("div[class=beatmapsets-search__filter-grid]").css("font-size","16px");








// alert(item.css("transform", "translateX(50px)"));
// d.remove();

// let iframe = $("div");
// // iframe.remove();
// if(iframe.attr("id")=="animation_container")
// {
// 	iframe.remove();
// }
	// let img = $("a");
	// if(img.attr("class"=="page_post_sized_thumbs clear_fix"))
	// {
	// 	img.remove();
	// }
// setInterval(main,1)

// function main()
// {
// 	let iframe = $("div");

// 	if(iframe.attr("aria-label")=="реклама")
// 	{
// 		iframe.remove();
// 	}
// }