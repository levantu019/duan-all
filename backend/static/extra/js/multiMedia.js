// 
function getValueFields(id_model, id_element){
    let $ = django.jQuery;
    let base_url = window.location.origin;
    let choices = '<option value="" selected="">---------</option>'

    $.ajax({
        type: "GET",
        url: `${base_url}/multimedia/other/app-model/${id_model}`
    })
    .done(res => {
        $.ajax({
            type: "GET",
            url: `${base_url}/multimedia/other/value-fields/${res.app_label}/${res.model_name}/maNhanDang`
        })
        .done(res => {
            $.each(res, function(i, item){
                choices += '<option value="'+ item.maNhanDang +'">'+ item.maNhanDang +'</option>'
            });
            $(`#${id_element}`).html(choices);
        })
        .fail(() => {
            $(`#${id_element}`).html(choices);
        })
    })
    .fail(() => {
        $(`#${id_element}`).html(choices);
    })
}