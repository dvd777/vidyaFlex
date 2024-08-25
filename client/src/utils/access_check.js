function accessCheck() {
  const accessToken = localStorage.getItem("access");
  return accessToken ? true : false;
}

function roleCheck() {
  const role = localStorage.getItem("role");
  return role === "true" ? false : true;
}

export { accessCheck, roleCheck };
