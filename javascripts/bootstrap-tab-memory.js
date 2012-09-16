// Remember bootstrap tabs between page visits.
$(function () {
    $('.nav-tabs').find('a:first').tab('show');
    
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
        $('.nav-tabs li a.' + preferredTab).tab('show');
    }

    $('a[data-toggle="tab"]').on('shown', function (e) {
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