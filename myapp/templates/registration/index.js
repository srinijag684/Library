 //takes in the name of cookie, value to be stored in the cookie,
//number of days for cookie to expire
function setCookie(cookieName, cookieValue, expirationDays){
    const d = new Date(); //create a date object
    d.setTime(d.getTime() + (expirationDays * 24 * 60 * 60 * 1000)); // calculate expiration time
    const expires = "expires = " + d.toUTCString(); // convert to UTC format
    document.cookie = cookieName + "=" + cookieValue + ";" + expires + ";path=/" //set cookie
}

function getCookie(cookieName){
    // this create a string that will search for within the 'document.cookie' string
    const name = cookieName + "="; 
    //handle special characters
    const decodedCookie = decodeURIComponent(document.cookie);
    //splits cookie string into an array individual cookies
    const cookieArray = decodedCookie.split(';');
    //iterates through the array of cookies, trims any leading spaces, and checks if the current 
    //cookie starts with the desired 'name'.If found, it returns the value of the cookie
    for (let i = 0; i < cookieArray.length; i++){
        let cookie = cookieArray[i];
        while (cookie.charAt(0) === ' '){
            cookie = cookie.substring(1);
        }
        if (cookie.indexOf(name) === 0){
            return cookie.substring(name.length, cookie.length);
        }
    }
    //return an empty string if cookie is not found
    return ""
}

function deleteCookie(cookieName){
    //deletes cookie by setting its expiration time to a past date
    document.cookie = cookieName + "=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
}

setCookie("username", "John Doe", 30);
const username = getCookie("username");
console.log(username);