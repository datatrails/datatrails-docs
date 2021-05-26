import Clipboard from 'clipboard';

var clipboard = new Clipboard('.btn-clipboard', {
    target: function (trigger) {
      return trigger.nextElementSibling;
    },
  });

clipboard.on('success', function(e) {
    
    console.info('Action:', e.action);
    console.info('Text:', e.text);
    console.info('Trigger:', e.trigger);
    e.clearSelection();
});

clipboard.on('error', function(e) {
    console.error('Action:', e.action);
    console.error('Trigger:', e.trigger);
});


var pre = document.getElementsByTagName('pre');
for (var i = 0; i < pre.length; i++) {
    var isLanguage = pre[i].children[0].className.indexOf('language-');
    if ( isLanguage === 0 ) {
        var button     = document.createElement("button")
            button.className='btn-clipboard btn btn-link d-none d-lg-block'
            button.innerHTML='<span class="copy-status"></span>'
            pre[i].prepend(button)
        }
}