jQuery(function ($) {
    // デフォルトの設定を変更
    $.extend($.fn.dataTable.defaults, {
        language: {
            url: "http://cdn.datatables.net/plug-ins/9dcbecd42ad/i18n/Japanese.json"
        }
    });
    $("#post_list").DataTable({
        "searching": true,     //検索機能
        "paging": true,      //ページング機能
        "ordering": true,      //ソート機能
        "lengthChange": true,  //件数切り替え機能

    }).columns.adjust();
});
