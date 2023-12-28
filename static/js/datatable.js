$(document).ready(function () {
    $('#myTable').dataTable({
        responsive: true,
        language: {
            url: '//cdn.datatables.net/plug-ins/1.13.7/i18n/pt-BR.json',
        },
        "lengthChange": false,
        order: [[1, 'asc']],
    });

});

