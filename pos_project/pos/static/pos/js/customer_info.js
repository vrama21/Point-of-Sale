document.getElementById('customer-status-toggle').onclick = function() {
    toggleDiv('customer-status');
}
document.getElementById('previous-orders-toggle').onclick = function() {
    toggleDiv('previous-orders');
}

function toggleDiv(id) {
    const parent_div = document.getElementById('customer-info-optional-container')
    const target_div  = document.getElementById(id);
    const nodes = parent_div.children;


    parent_div.style.display = 'none';
    for (i = 0; i < nodes.length; i++) {
        nodes[i].style.display = 'none';
    }

    if (target_div.style.display == 'none' || target_div.style.display == '') {
        parent_div.style.display = 'block';
        target_div.style.display = 'block';
    } 
    else {
        parent_div.style.display = 'none';
        target_div.style.display = 'none';
    }
}

function toggleDiv(id) {
    const parent_div = document.getElementById('customer-info-optional-container')
    const target_div = document.getElementById(id);
    const nodes = parent_div.children;

    if (parent_div.style.display == 'none' || parent_div.style.display == '') {
        for (i = 0; i < nodes.length; i++) {
            nodes[i].style.display = 'none';
        }
        parent_div.style.display = 'block';
        target_div.style.display = 'block'
    } else {
        parent_div.style.display = 'none';
        for (i = 0; i < nodes.length; i++) {
            nodes[i].style.display = 'none';
        }
    }
    
    
}

