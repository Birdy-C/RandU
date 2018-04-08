$(".hover-menu li").hover(
    function () {
        $(this).find("em").animate({ opacity: "show", top: "24%" }, "slow");
    },
    function () {
        $(this).find("em").animate({ opacity: "hide", top: "27%" }, "fast");
    },
);

$("#team-part").hover(
    function () {
        $("#team-pic1").animate({ opacity: "1" }, "slow");
    },
    function () {
        $("#team-pic1").animate({ opacity: "0" }, "slow");
    },

)