function set_maNhanDang_madt(maDoiTuong){
    let $ = django.jQuery;
    const index = $('#ma-nhan-dang').attr('data-index');
    const scale = $('#ma-nhan-dang').attr('data-scale');
    const maTinh = $('#ma-tinh').val();

    const indentifier = scale + maTinh + maDoiTuong + index;

    if (maDoiTuong != '') $('#ma-nhan-dang').val(indentifier);
    else $('#ma-nhan-dang').val('');
}

function set_maNhanDang_matinh(maTinh) {
    let $ = django.jQuery;
    var new_maDoiTuong = '';
    const maDoiTuong = $('#ma-nhan-dang').val();

    if (maDoiTuong != ''){
        if (maTinh.length === 16){
            new_maDoiTuong = maDoiTuong.slice(0, 4) + maTinh + maDoiTuong.slice(4);
        }
        else{
            new_maDoiTuong = maDoiTuong.slice(0, 4) + maTinh + maDoiTuong.slice(6);
        }
        $('#ma-nhan-dang').val(new_maDoiTuong);
    }
}