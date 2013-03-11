// Remember foundation sections between page visits.
// To select: $($('a')[6]).click(); // Just click the tab.

$(function () {
    // Select preferred tabs
    var preferredTabs;
    try {
        preferredTabs = JSON.parse(window.localStorage.getItem('preferredTabs'));
    } catch(ignore) {
    }
    if(!preferredTabs) {
        preferredTabs = {};
    }

    for(var preferredTab in preferredTabs) {
        console.log('TAB', preferredTab);
        //$('.nav-tabs li a.' + preferredTab).tab('show');
    }

    $('.section-container .content').on('shown', function (e) {
        console.log('shown');
        $(this).parent().siblings().find('a').each(function(_, a) {
            var unpreferred = a.className;
            if(unpreferred in preferredTabs) {
                delete preferredTabs[unpreferred];
            }
        });
        var selected = e.target.className;
        preferredTabs[selected] = selected;
        window.localStorage.setItem('preferredTabs', JSON.stringify(preferredTabs));
    });
});

function cb1(e) {
  console.log('CALLBACK-1', this, e);
}

function cb2(e) {
  console.log('CALLBACK-2', this, e);
}

$(document).foundation('section', {callback: cb1}, cb2);