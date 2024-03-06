export default function (context) {	
	if (process.client) {
		context.store.dispatch("auth/initAuth");
	} else {
		context.store.dispatch("auth/initAuth", context.req);
	}

}