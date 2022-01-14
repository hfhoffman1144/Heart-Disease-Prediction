$(document).ready(function(e) {

    $('#makePred').click(function() {

        $('#hfProb').empty();
        $('#hfPred').empty();

        var sex = $('#sex').val();
        var restingECG = $('#restingECG').val();
        var cpt = $('#chestPainType').val();
        var exerciseAngina = $('#exerciseAngina').val();
        var sts = $('#stSlope').val();
        var age = $('#age').val();
        var bp = $('#restingBP').val();
        var chol = $('#cholesterol').val();
        var bs = $('#fastingBS').val();
        var maxHR = $('#maxHR').val();
        var oldpeak = $('#oldpeak').val();

        var inputData = {
            'sex': sex,
            'restingECG': restingECG,
            'cpt': cpt,
            'exerciseAngina': exerciseAngina,
            'sts': sts,
            'age': age,
            'bp': bp,
            'chol': chol,
            'bs': bs,
            'maxHR': maxHR,
            'oldpeak': oldpeak
        };

        $.ajax({
            url: 'main/api/make_prediction',
            data: inputData,
            type: 'post',
            success: function(response) {
                $('#hfProb').append(`<p style="color:white;">Patient has a ${response['pred']} probability of heart failure</p>`)

                var figure = JSON.parse(response['plot']);
                Plotly.newPlot('hfPlot', figure.data, figure.layout, {
                    displayModeBar: false,
                    responsive: true
                });

            }
        })
    });


});