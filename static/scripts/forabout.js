$(".hover-menu li").hover(
    function () {
        $(this).find("em").animate({ opacity: "show", top: "18%" }, "slow");
    },
    function () {
        $(this).find("em").animate({ opacity: "hide", top: "21%" }, "fast");
    },
);