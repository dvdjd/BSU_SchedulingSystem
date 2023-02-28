jQuery(document).ready(function($) {
    $("#id_course_code").on('change', function() {
        if ($(this).val() != '') {
            $.ajax({
                method: 'POST',
                url: '/populate_programcode',
                data: {
                    course_code: $("#id_course_code").find(":selected").text()
                },
                headers: {
                    'X-CSRFToken': $('input[name=csrfmiddlewaretoken]').val()
                },
                success: function(data) {
                    $("#id_program_code").val(data);
                },
                error: function(data) {
                    console.log(data)
                }
            });
        }
    });
});