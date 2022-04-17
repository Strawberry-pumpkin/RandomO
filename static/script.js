function search() {
    var btn = document.getElementById('srch');
    if (btn.className == 'fa-solid fa-magnifying-glass search fa-2x') {
        btn.className = 'fa-solid fa-xmark fa-2x search';
        document.getElementById('srch-bar').style.display = 'block';
    } else {
        btn.className = 'fa-solid fa-magnifying-glass search fa-2x';
        document.getElementById('srch-bar').style.display = 'none';
    }

}

function search2() {
    var btn = document.getElementById('srch2');
    if (btn.className == 'fa-solid fa-magnifying-glass search fa-2x') {
        btn.className = 'fa-solid fa-xmark fa-2x search';
        document.getElementById('srch-bar').style.display = 'block';
        document.getElementById('srch2').style.top = '5vw';

    } else {
        btn.className = 'fa-solid fa-magnifying-glass search fa-2x';
        document.getElementById('srch-bar').style.display = 'none';
        document.getElementById('srch2').style.top = '0';

    }

}
$(function() {
    $(document).scroll(function() {
        var $nav = $(".resp-brn");
        var $nav2 = $(".navbr");
        $nav.addClass('fix-nav');
        $nav2.addClass('fix-nav2');
    });
    $(document).scrollTop(function() {
        var $nav = $(".resp-brn");
        var $nav2 = $(".navbr");
        if (document.body.scrollTop < 10) {
            $nav.css('background', 'rgba(255, 255, 255, 0.1)');
            $nav2.css('background', 'rgba(255,255,255,0.1')
        }
    });
});

function resp() {
    if (document.getElementById('responsive').style.display == 'block') {
        document.getElementById('responsive').style.display = 'none';
        document.getElementById('respo').className = 'fa-solid fa-bars fa-2x';

    } else {
        document.getElementById('responsive').style.display = 'block';
        document.getElementById('respo').className = 'fa-solid fa-xmark fa-2x fa-flip';

    }
}

function prof() {
    var profile_button = document.getElementById('profile');
    if (profile_button.style.display == 'block') {
        profile_button.style.display = 'none';
    } else {
        profile_button.style.display = 'block';
    }
}

function add_points(score) {
    var total_points = document.getElementById('points');
    total_points.value = score;

}

function myFunction() {
    // Declare variables
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    table = document.getElementById("table");
    tr = table.getElementsByTagName("tr");

    // Loop through all table rows, and hide those who don't match the search query
    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[2];
        if (td) {
            txtValue = td.textContent || td.innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
                document.getElementById('headers').display = ''
            }
        }
    }
}

function contact() {
    var platform = document.getElementById('contact')
    if (platform.style.display == 'block') {
        platform.style.display = 'none'
    } else {
        platform.style.display = 'block'
    }
}


function rain(emoji) {
    document.getElementById(emoji).style.display = 'block';
    if (emoji == 'laugh') {
        document.getElementById('surprise').style.display = 'none';
        document.getElementById('neutral').style.display = 'none';
        document.getElementById('sad').style.display = 'none';
        document.getElementById('angry').style.display = 'none';
    } else if (emoji == 'surprise') {
        document.getElementById('laugh').style.display = 'none';
        document.getElementById('neutral').style.display = 'none';
        document.getElementById('sad').style.display = 'none';
        document.getElementById('angry').style.display = 'none';

    } else if (emoji == 'neutral') {
        document.getElementById('laugh').style.display = 'none';
        document.getElementById('surprise').style.display = 'none';
        document.getElementById('sad').style.display = 'none';
        document.getElementById('angry').style.display = 'none';

    } else if (emoji == 'sad') {
        document.getElementById('laugh').style.display = 'none';
        document.getElementById('surprise').style.display = 'none';
        document.getElementById('neutral').style.display = 'none';
        document.getElementById('angry').style.display = 'none';

    } else if (emoji == 'angry') {
        document.getElementById('laugh').style.display = 'none';
        document.getElementById('surprise').style.display = 'none';
        document.getElementById('neutral').style.display = 'none';
        document.getElementById('sad').style.display = 'none';

    }
    setInterval(function() {
        document.getElementById(emoji).style.display = 'none'
    }, 5000)

}


function reveal() {
    document.getElementById('resp').click();
}

function change_profile(){
    document.getElementById('file').click();
}

function submit_profile(){
    document.getElementById('submit-img').click();
}
