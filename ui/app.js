(function () {
    const form = document.getElementById('calc-form');
    const input = document.getElementById('id-input');
    const result = document.getElementById('result');
    const go = document.getElementById('go');

    function showMessage(html, ok = true) {
        result.innerHTML = html;
        result.style.borderLeft = ok ? '4px solid #7c3aed' : '4px solid #ef4444';
    }

    async function calculate(id) {
        showMessage('Calculating…', true);
        try {
            const res = await fetch('/api/checkdigit', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ id_number: id })
            });
            const j = await res.json();
            if (!res.ok || !j.ok) {
                showMessage('<strong>Error:</strong> ' + (j && j.error ? j.error : res.statusText), false);
                return;
            }
            showMessage(`<strong>Check digit:</strong> <span style="font-size:20px;margin-left:8px;">${j.check_digit}</span>`, true);
        } catch (err) {
            showMessage('<strong>Network error</strong>', false);
            console.error(err);
        }
    }

    form.addEventListener('submit', ev => {
        ev.preventDefault();
        const v = input.value.trim();
        if (!v) { showMessage('Please enter an ID number', false); return; }
        calculate(v);
    });

    // quick enter handler
    input.addEventListener('keydown', e => { if (e.key === 'Enter') { e.preventDefault(); go.click(); } });

})();