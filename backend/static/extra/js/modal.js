django.jQuery(document).ready(function() {
    let $ = django.jQuery;
    let base_url = window.location.origin;
    let choices = '<option value="" selected="">---------</option>'

    // Sự kiện khi bấm button mở modal change field
    // Đặt tất cả input, href về null
    // Tải tất cả các trường thuộc model hiện tài về
    $("#change-field-modal").on("click", e => {
        $("#mymodal-field-id").val('');
        $("#mymodal-field-name").val('');
        $("#mymodal-field-datatype").val('');
        $("#mymodal-field-description").val('');
        $("#mymodal-field-display-order").val('');
        $("#mymodal-field-required").prop("checked", false);
        $("#btn-delete-attribute").attr('href', "");

        let app_model = $(e.target).attr("data-appmodel");

        $.ajax({
            type: "GET",
            url: `${base_url}/eav/attr/attr-by-entity/${app_model}`
        })
        .done(res => {
            $.each(res.data, function(i, item){
                choices += `<option value='${item.id}' data-name='${item.name}' data-datatype='${item.datatype}' data-description='${item.description}' data-displayorder='${item.display_order}' data-required=${item.required}> ${item.name} </option>`
            });
            $('#mymodal-list-added-fields').html(choices);
        })
        .fail(() => {
            $('#mymodal-list-added-fields').html(choices);
        })
    })

    // Khi lựa chọn field để chỉnh sửa, cập nhật giá trị các input và href
    $("#mymodal-list-added-fields").change(e => {
        const selected = $("#mymodal-list-added-fields option:selected");
        let required = selected.attr('data-required');

        $("#mymodal-field-id").val(selected.attr('value'));
        $("#mymodal-field-name").val(selected.attr('data-name'));
        $("#mymodal-field-datatype").val(selected.attr('data-datatype'));
        $("#mymodal-field-description").val(selected.attr('data-description'));
        $("#mymodal-field-display-order").val(selected.attr('data-displayorder'));

        if (required === "true") $("#mymodal-field-required").prop("checked", true);
        else $("#mymodal-field-required").prop("checked", false);

        $("#btn-delete-attribute").attr('href', `/eav/attr/delete-attr/${selected.attr('value')}`);
    })


    // Để đảm bảo khi chưa có field nào được chọn, chặn hành động của thẻ delete
    $("#btn-delete-attribute").on('click', e => {
        if ($("#mymodal-field-id").val() === '')
        e.preventDefault();
    })
})
// var change_modal = 'False';
// function enable_add_modal()

