import { createStore } from 'vuex'

export default createStore({
    state: {
        connection: "",
        session: { "apellido": null, "contra": null, "email":null, "id": null, "nombre": null, "posicion": null, "tipo": null}
    },
    mutations: {
        SET_CONNECTION(state) {
            let conn
            if (location.hostname === "localhost" || location.hostname === "127.0.0.1") {
                conn = "http://localhost:4000/"
            }
            else {
                conn = "api/"
            }
            state.connection = conn
        },
    },
    actions: {
    },
    modules: {
    }
})
