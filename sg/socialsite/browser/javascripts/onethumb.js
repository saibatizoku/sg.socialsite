jQuery(function(jq){

    jq('#content').delegate(".thumb-rating form input", "click", (function(event){
        event.preventDefault();
        var form = jq(this).closest('form');
        var action = jq(this).attr('name');
        var summary = form.siblings('.like-summary');
        var upResults = summary.find('.total-thumbs-up .tally-total');
        var downResults = summary.find('.total-thumbs-down .tally-total');
        var totalResults = summary.find('.total-thumbs .tally-total');
        if (form){
            jq.post(form.attr("action"),action+'=FOOBAR', 
                function(data) {
                    /* update the text */
                    totalResults.text(data.ups-data.downs);

                    /* update the class */
                    if (action == 'form.lovinit'){
                        form.find('.thumbs-down').removeClass('selected');
                        form.find('.thumbs-up').addClass('selected');
                    } else {
                        form.find('.thumbs-up').removeClass('selected');
                        form.find('.thumbs-down').addClass('selected');
                    }
                }, 'json');

        }
    }));
});