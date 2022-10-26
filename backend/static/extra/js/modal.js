// Sự kiện modal sử dụng cho làm việc với custom field
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
            $('#loai-tbkt').html(choices);
        })
        .fail(() => {
            $('#loai-tbkt').html(choices);
        })
    })

    // Khi lựa chọn field để chỉnh sửa, cập nhật giá trị các input và href
    $("#loai-tbkt").change(e => {
        const selected = $("#loai-tbkt option:selected");
        let required = selected.attr('data-required');

        $("#mymodal-field-id").val(selected.attr('value'));
        $("#mymodal-field-name").val(selected.attr('data-name'));
        $("#mymodal-field-datatype").val(selected.attr('data-datatype'));
        $("#mymodal-field-description").val(selected.attr('data-description'));
        $("#mymodal-field-display-order").val(selected.attr('data-displayorder'));

        if (required === "true") $("#mymodal-field-required").prop("checked", true);
        else $("#mymodal-field-required").prop("checked", false);

        // $("#btn-delete-attribute").attr('href', `/eav/attr/delete-attr/${selected.attr('value')}`);
        $("#btn-delete-attribute").attr('href', `/admin/eav/attribute/${selected.attr('value')}/delete`);
    })


    // Để đảm bảo khi chưa có field nào được chọn, chặn hành động của thẻ delete
    $("#btn-delete-attribute").on('click', e => {
        if ($("#mymodal-field-id").val() === '')
        e.preventDefault();
    })
})
// var change_modal = 'False';
// function enable_add_modal()




// Sự kiện modal sử dụng cho làm việc với thống kê
django.jQuery(document).ready(function() {
    let $ = django.jQuery;
    let base_url = window.location.origin;

    // 
    var type_thongke = '';
    var title_thongke = '';
    var app_model = '';
    $(".thongke").on('click', function(e) {
        type_thongke = $(this).attr("data-type");
        title_thongke = $(this).attr("data-title");
        app_model = $(this).attr("data-appmodel");
        $("#select-thongke").html(title_thongke);

        // 
        let choices = '<option value="" selected="">---------</option>'

        $.ajax({
            type: "GET",
            url: `${base_url}/core/statistic-type/${type_thongke}`
        })
        .done(res => {
            $.each(res.data, function(i, item){
                choices += `<option value='${item.value}'> ${item.text} </option>`
            });
            $('#value-thongke').html(choices);
        })
        .fail(() => {
            $('#value-thongke').html(choices);
        })
    })
   

    // Sự kiện khi chọn loại trang bị, vẽ biểu đồ
    var myChart;
    $('#value-thongke').change(function(e){
        $.ajax({
            type: "GET",
            url: `${base_url}/core/statistic-value/${type_thongke}/${$(this).val()}/${app_model}`
        })
        .done(res => {
            if (myChart) myChart.destroy();
            myChart = createPieChart("chart", res.data, randomColor(Object.keys(res.data).length), title_thongke);
        })
        .fail(() => {
            
        })
    })
})