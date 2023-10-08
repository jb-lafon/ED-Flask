// Mark: SVG Loader

function apiCall(apiUrl){
    $.getJSON(apiUrl, function (data) {
        $('#length').html('Systems Found: '+data.length);
        return data;
    });
    console.log('baop');
}


$('#s2r-submit').click(function () {
    let img = '<svg style="height:170px" viewbox="0 0 40 40" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">\n' +
        '\n' +
        '  <style type="text/css" >\n' +
        '      <![CDATA[\n' +
        '\n' +
        '        @keyframes outer {\n' +
        '          0% {\n' +
        '            opacity: 0.3;\n' +
        '          }\n' +
        '          20% {\n' +
        '            opacity: 1;\n' +
        '          }\n' +
        '          100% {\n' +
        '            opacity: 0.3;\n' +
        '          }\n' +
        '        }\n' +
        '        @keyframes inner {\n' +
        '          0% {\n' +
        '            opacity: 0.4;\n' +
        '          }\n' +
        '          20% {\n' +
        '            opacity: 1;\n' +
        '          }\n' +
        '          100% {\n' +
        '            opacity: 0.4;\n' +
        '          }\n' +
        '        }\n' +
        '        .l1 {\n' +
        '          animation: outer 1000ms linear infinite;\n' +
        '        }\n' +
        '        .l2 {\n' +
        '          animation: inner 1000ms linear infinite;\n' +
        '        }\n' +
        '        .d19 {\n' +
        '          opacity: 1;\n' +
        '          animation-delay: 1000ms;\n' +
        '        }\n' +
        '        .d18 {\n' +
        '          opacity: 0.94736842;\n' +
        '          animation-delay: 947.36842105ms;\n' +
        '        }\n' +
        '        .d17 {\n' +
        '          opacity: 0.89473684;\n' +
        '          animation-delay: 894.73684211ms;\n' +
        '        }\n' +
        '        .d16 {\n' +
        '          opacity: 0.84210526;\n' +
        '          animation-delay: 842.10526316ms;\n' +
        '        }\n' +
        '        .d15 {\n' +
        '          opacity: 0.78947368;\n' +
        '          animation-delay: 789.47368421ms;\n' +
        '        }\n' +
        '        .d14 {\n' +
        '          opacity: 0.73684211;\n' +
        '          animation-delay: 736.84210526ms;\n' +
        '        }\n' +
        '        .d13 {\n' +
        '          opacity: 0.68421053;\n' +
        '          animation-delay: 684.21052632ms;\n' +
        '        }\n' +
        '        .d12 {\n' +
        '          opacity: 0.63157895;\n' +
        '          animation-delay: 631.57894737ms;\n' +
        '        }\n' +
        '        .d11 {\n' +
        '          opacity: 0.57894737;\n' +
        '          animation-delay: 578.94736842ms;\n' +
        '        }\n' +
        '        .d10 {\n' +
        '          opacity: 0.52631579;\n' +
        '          animation-delay: 526.31578947ms;\n' +
        '        }\n' +
        '        .d9 {\n' +
        '          opacity: 0.47368421;\n' +
        '          animation-delay: 473.68421053ms;\n' +
        '        }\n' +
        '        .d8 {\n' +
        '          opacity: 0.42105263;\n' +
        '          animation-delay: 421.05263158ms;\n' +
        '        }\n' +
        '        .d7 {\n' +
        '          opacity: 0.36842105;\n' +
        '          animation-delay: 368.42105263ms;\n' +
        '        }\n' +
        '        .d6 {\n' +
        '          opacity: 0.31578947;\n' +
        '          animation-delay: 315.78947368ms;\n' +
        '        }\n' +
        '        .d5 {\n' +
        '          opacity: 0.26315789;\n' +
        '          animation-delay: 263.15789474ms;\n' +
        '        }\n' +
        '        .d4 {\n' +
        '          opacity: 0.21052632;\n' +
        '          animation-delay: 210.52631579ms;\n' +
        '        }\n' +
        '        .d3 {\n' +
        '          opacity: 0.15789474;\n' +
        '          animation-delay: 157.89473684ms;\n' +
        '        }\n' +
        '        .d2 {\n' +
        '          opacity: 0.10526316;\n' +
        '          animation-delay: 105.26315789ms;\n' +
        '        }\n' +
        '        .d1 {\n' +
        '          opacity: 0.05263158;\n' +
        '          animation-delay: 52.63157895ms;\n' +
        '        }\n' +
        '        svg {\n' +
        '          fill: #ff7100;\n' +
        '        }\n' +
        '\n' +
        '      ]]>\n' +
        '    </style>\n' +
        '\n' +
        '  <path d="m5,8l5,8l5,-8z" class="l1 d1" />\n' +
        '  <path d="m5,8l5,-8l5,8z" class="l1 d2" />\n' +
        '  <path d="m10,0l5,8l5,-8z" class="l1 d3" />\n' +
        '  <path d="m15,8l5,-8l5,8z" class="l1 d4" />\n' +
        '  <path d="m20,0l5,8l5,-8z" class="l1 d5" />\n' +
        '  <path d="m25,8l5,-8l5,8z" class="l1 d6" />\n' +
        '  <path d="m25,8l5,8l5,-8z" class="l1 d7" />\n' +
        '  <path d="m30,16l5,-8l5,8z" class="l1 d8" />\n' +
        '  <path d="m30,16l5,8l5,-8z" class="l1 d9" />\n' +
        '  <path d="m25,24l5,-8l5,8z" class="l1 d10" />\n' +
        '  <path d="m25,24l5,8l5,-8z" class="l1 d11" />\n' +
        '  <path d="m20,32l5,-8l5,8z" class="l1 d13" />\n' +
        '  <path d="m15,24l5,8l5,-8z" class="l1 d14" />\n' +
        '  <path d="m10,32l5,-8l5,8z" class="l1 d15" />\n' +
        '  <path d="m5,24l5,8l5,-8z" class="l1 d16" />\n' +
        '  <path d="m5,24l5,-8l5,8z" class="l1 d17" />\n' +
        '  <path d="m0,16l5,8l5,-8z" class="l1 d18" />\n' +
        '  <path d="m0,16l5,-8l5,8z" class="l1 d20" />\n' +
        '  <path d="m10,16l5,-8l5,8z" class="l2 d0" />\n' +
        '  <path d="m15,8l5,8l5,-8z" class="l2 d3" />\n' +
        '  <path d="m20,16l5,-8l5,8z" class="l2 d6" />\n' +
        '  <path d="m20,16l5,8l5,-8z" class="l2 d9" />\n' +
        '  <path d="m15,24l5,-8l5,8z" class="l2 d12" />\n' +
        '  <path d="m10,16l5,8l5,-8z" class="l2 d15" />\n' +
        '</svg>';
    $('#loader').html(img);


    let sysName = encodeURIComponent($('#name').val());
    let minRad = encodeURIComponent($('#minRadius').val());
    let maxRad = encodeURIComponent($('#maxRadius').val());
    let url = 'https://www.edsm.net/api-v1/sphere-systems?systemName='+sysName+'&minRadius='+minRad+'&radius='+maxRad;
    apiCall(url);
});
// $("#s2r-submit").click(function () {
//     $("#loader").addClass("loading");
// });
//Todo-jb: SVG compatibility fix

