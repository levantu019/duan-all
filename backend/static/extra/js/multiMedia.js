//
function getValueFields(id_model, id_element, value_element) {
  let $ = django.jQuery;
  let base_url = window.location.origin;
  let choices = '<option value="" selected="">---------</option>';

  $.ajax({
    type: "GET",
    url: `${base_url}/multi-media/other/app-model/${id_model}`,
  })
    .done((res) => {
      $.ajax({
        type: "GET",
        url: `${base_url}/multi-media/other/value-fields/${res.app_label}/${res.model_name}/maNhanDang`,
      })
        .done((res) => {
          $.each(res, function (i, item) {
            if (item.maNhanDang == value_element)
              choices += `<option value="${item.maNhanDang}" selected> ${item.maNhanDang} </option>`;
            else
              choices += `<option value="${item.maNhanDang}"> ${item.maNhanDang} </option>`;
          });
          $(`#${id_element}`).html(choices);
        })
        .fail(() => {
          $(`#${id_element}`).html(choices);
        });
    })
    .fail(() => {
      $(`#${id_element}`).html(choices);
    });
}

// Sự kiện khi thay đổi lựa chọn loại nhóm thì sẽ tải tất cả model chưa được thêm vào bảng về
function getChoiceModels(app_label, id_element) {
  let $ = django.jQuery;
  let base_url = window.location.origin;
  let choices = '<option value="" selected="">---------</option>';

  $.ajax({
    type: "GET",
    url: `${base_url}/multi-media/other/choice-models/${app_label}`,
  })
    .done((res) => {
      $.each(res, function (i, item) {
        choices +=
          '<option value="' + item.name + '">' + item.label + "</option>";
      });
      $(`#${id_element}`).html(choices);
    })
    .fail(() => {
      $(`#${id_element}`).html(choices);
    });
}

//
