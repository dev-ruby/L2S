const change_url = (span, url) => {
    span.value = url
}


const copy = () => {
    const url_span = document.getElementsByClassName("sub_title")[0]
    const copy_button = document.getElementsByClassName("copy_button")[0]
    const url = url_span.innerHTML.trim()
    navigator.clipboard.writeText(url)
        .then(() => {
            const original = copy_button.value
            copy_button.value = "복사 성공"
            setTimeout(() => change_url(copy_button, original), 1000)
        })
        .catch(err => {
            const original = copy_button.value
            copy_button.value = "복사 실패"
            setTimeout(() => change_url(copy_button, original), 1000)
        })
}