import Cookies from "js-cookie";

const TokenKey = "Admin-Token";
const RefeshToken = "Refesh-Token";
const CCSession = "CC-Session";
export function getToken() {
  return Cookies.get(TokenKey);
}

export function getRefeshToken() {
  return Cookies.get(RefeshToken);
}

export function setToken(token, refeshToken) {
  if (Cookies.set(TokenKey, token))
    return Cookies.set(RefeshToken, refeshToken);
  else return false;
}

export function removeToken() {
  return Cookies.remove(TokenKey);
}

export function getCCSession() {
  return Cookies.get(CCSession);
}

export function setCCSession(session) {
  return Cookies.set(CCSession, session);
}

export function removeCCSession() {
  return Cookies.remove(CCSession);
}
