function getZodiac(year) {
    const zodiacs = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"];
    return zodiacs[(year - 4) % 12];
}

function calculate() {
    const dateStr = document.getElementById('date').value;
    try {
        let dateObj;
        if (dateStr.length === 8) {
            dateObj = new Date(dateStr.slice(0, 4), dateStr.slice(4, 6) - 1, dateStr.slice(6, 8));
        } else {
            dateObj = new Date(dateStr);
        }
        const options = { weekday: 'long' };
        const weekday = new Intl.DateTimeFormat('ja-JP', options).format(dateObj);
        const zodiac = getZodiac(dateObj.getFullYear());
        const resultStr = `${dateStr} (${weekday}) - 干支: ${zodiac}`;
        document.getElementById('result').innerText = resultStr;
    } catch (error) {
        alert("日付の形式が正しくありません。yyyy/mm/dd または yyyymmdd の形式で入力してください。");
    }
}

function copyToClipboard() {
    const result = document.getElementById('result').innerText;
    navigator.clipboard.writeText(result).then(() => {
        alert('結果がクリップボードにコピーされました。');
    });
}
