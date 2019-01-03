--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner:
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner:
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


--
-- Name: postgis; Type: EXTENSION; Schema: -; Owner:
--

CREATE EXTENSION IF NOT EXISTS postgis WITH SCHEMA public;


--
-- Name: EXTENSION postgis; Type: COMMENT; Schema: -; Owner:
--

COMMENT ON EXTENSION postgis IS 'PostGIS geometry, geography, and raster spatial types and functions';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: wx_group; Type: TABLE; Schema: public; Owner: wxshop
--

CREATE TABLE public.wx_group (
    id integer NOT NULL,
    name character varying(20) NOT NULL,
    "desc" character varying(200),
    create_at timestamp without time zone,
    update_at timestamp without time zone
);


ALTER TABLE public.wx_group OWNER TO wxshop;

--
-- Name: wx_group_id_seq; Type: SEQUENCE; Schema: public; Owner: wxshop
--

CREATE SEQUENCE public.wx_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.wx_group_id_seq OWNER TO wxshop;

--
-- Name: wx_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wxshop
--

ALTER SEQUENCE public.wx_group_id_seq OWNED BY public.wx_group.id;


--
-- Name: wx_group_perm_relation; Type: TABLE; Schema: public; Owner: wxshop
--

CREATE TABLE public.wx_group_perm_relation (
    id integer NOT NULL,
    group_id integer NOT NULL,
    perm_id integer NOT NULL,
    create_at timestamp without time zone,
    update_at timestamp without time zone
);


ALTER TABLE public.wx_group_perm_relation OWNER TO wxshop;

--
-- Name: wx_group_perm_relation_id_seq; Type: SEQUENCE; Schema: public; Owner: wxshop
--

CREATE SEQUENCE public.wx_group_perm_relation_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.wx_group_perm_relation_id_seq OWNER TO wxshop;

--
-- Name: wx_group_perm_relation_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wxshop
--

ALTER SEQUENCE public.wx_group_perm_relation_id_seq OWNED BY public.wx_group_perm_relation.id;


--
-- Name: wx_perm; Type: TABLE; Schema: public; Owner: wxshop
--

CREATE TABLE public.wx_perm (
    id integer NOT NULL,
    name character varying(20) NOT NULL,
    "desc" character varying(200),
    create_at timestamp without time zone,
    update_at timestamp without time zone
);


ALTER TABLE public.wx_perm OWNER TO wxshop;

--
-- Name: wx_perm_id_seq; Type: SEQUENCE; Schema: public; Owner: wxshop
--

CREATE SEQUENCE public.wx_perm_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.wx_perm_id_seq OWNER TO wxshop;

--
-- Name: wx_perm_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wxshop
--

ALTER SEQUENCE public.wx_perm_id_seq OWNED BY public.wx_perm.id;


--
-- Name: wx_user; Type: TABLE; Schema: public; Owner: wxshop
--

CREATE TABLE public.wx_user (
    id integer NOT NULL,
    username character varying(50) NOT NULL,
    password character varying(200) NOT NULL,
    fullname character varying(100) DEFAULT NULL,
    is_superuser boolean,
    is_active boolean,
    email character varying(254),
    phone character varying(20),
    create_at timestamp without time zone,
    update_at timestamp without time zone
);


ALTER TABLE public.wx_user OWNER TO wxshop;

--
-- Name: wx_user_group_relation; Type: TABLE; Schema: public; Owner: wxshop
--

CREATE TABLE public.wx_user_group_relation (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL,
    create_at timestamp without time zone,
    update_at timestamp without time zone
);


ALTER TABLE public.wx_user_group_relation OWNER TO wxshop;

--
-- Name: wx_user_group_relation_id_seq; Type: SEQUENCE; Schema: public; Owner: wxshop
--

CREATE SEQUENCE public.wx_user_group_relation_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.wx_user_group_relation_id_seq OWNER TO wxshop;

--
-- Name: wx_user_group_relation_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wxshop
--

ALTER SEQUENCE public.wx_user_group_relation_id_seq OWNED BY public.wx_user_group_relation.id;


--
-- Name: wx_user_id_seq; Type: SEQUENCE; Schema: public; Owner: wxshop
--

CREATE SEQUENCE public.wx_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.wx_user_id_seq OWNER TO wxshop;

--
-- Name: wx_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wxshop
--

ALTER SEQUENCE public.wx_user_id_seq OWNED BY public.wx_user.id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: wxshop
--

ALTER TABLE ONLY public.wx_group ALTER COLUMN id SET DEFAULT nextval('public.wx_group_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: wxshop
--

ALTER TABLE ONLY public.wx_group_perm_relation ALTER COLUMN id SET DEFAULT nextval('public.wx_group_perm_relation_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: wxshop
--

ALTER TABLE ONLY public.wx_perm ALTER COLUMN id SET DEFAULT nextval('public.wx_perm_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: wxshop
--

ALTER TABLE ONLY public.wx_user ALTER COLUMN id SET DEFAULT nextval('public.wx_user_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: wxshop
--

ALTER TABLE ONLY public.wx_user_group_relation ALTER COLUMN id SET DEFAULT nextval('public.wx_user_group_relation_id_seq'::regclass);


--
-- Data for Name: wx_group; Type: TABLE DATA; Schema: public; Owner: wxshop
--

COPY public.wx_group (id, name, "desc", create_at, update_at) FROM stdin;
\.


--
-- Name: wx_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wxshop
--

SELECT pg_catalog.setval('public.wx_group_id_seq', 1, false);


--
-- Data for Name: wx_group_perm_relation; Type: TABLE DATA; Schema: public; Owner: wxshop
--

COPY public.wx_group_perm_relation (id, group_id, perm_id, create_at, update_at) FROM stdin;
\.


--
-- Name: wx_group_perm_relation_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wxshop
--

SELECT pg_catalog.setval('public.wx_group_perm_relation_id_seq', 1, false);


--
-- Data for Name: wx_perm; Type: TABLE DATA; Schema: public; Owner: wxshop
--

COPY public.wx_perm (id, name, "desc", create_at, update_at) FROM stdin;
\.


--
-- Name: wx_perm_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wxshop
--

SELECT pg_catalog.setval('public.wx_perm_id_seq', 1, false);


--
-- Data for Name: wx_user; Type: TABLE DATA; Schema: public; Owner: wxshop
--

COPY public.wx_user (id, username, password, is_superuser, is_active, email, phone, create_at, update_at) FROM stdin;
\.


--
-- Data for Name: wx_user_group_relation; Type: TABLE DATA; Schema: public; Owner: wxshop
--

COPY public.wx_user_group_relation (id, user_id, group_id, create_at, update_at) FROM stdin;
\.


--
-- Name: wx_user_group_relation_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wxshop
--

SELECT pg_catalog.setval('public.wx_user_group_relation_id_seq', 1, false);


--
-- Name: wx_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wxshop
--

SELECT pg_catalog.setval('public.wx_user_id_seq', 1, false);


--
-- Name: wx_group_name_key; Type: CONSTRAINT; Schema: public; Owner: wxshop
--

ALTER TABLE ONLY public.wx_group
    ADD CONSTRAINT wx_group_name_key UNIQUE (name);


--
-- Name: wx_group_perm_relation_pkey; Type: CONSTRAINT; Schema: public; Owner: wxshop
--

ALTER TABLE ONLY public.wx_group_perm_relation
    ADD CONSTRAINT wx_group_perm_relation_pkey PRIMARY KEY (id);


--
-- Name: wx_group_pkey; Type: CONSTRAINT; Schema: public; Owner: wxshop
--

ALTER TABLE ONLY public.wx_group
    ADD CONSTRAINT wx_group_pkey PRIMARY KEY (id);


--
-- Name: wx_perm_name_key; Type: CONSTRAINT; Schema: public; Owner: wxshop
--

ALTER TABLE ONLY public.wx_perm
    ADD CONSTRAINT wx_perm_name_key UNIQUE (name);


--
-- Name: wx_perm_pkey; Type: CONSTRAINT; Schema: public; Owner: wxshop
--

ALTER TABLE ONLY public.wx_perm
    ADD CONSTRAINT wx_perm_pkey PRIMARY KEY (id);


--
-- Name: wx_user_email_key; Type: CONSTRAINT; Schema: public; Owner: wxshop
--

ALTER TABLE ONLY public.wx_user
    ADD CONSTRAINT wx_user_email_key UNIQUE (email);


--
-- Name: wx_user_group_relation_pkey; Type: CONSTRAINT; Schema: public; Owner: wxshop
--

ALTER TABLE ONLY public.wx_user_group_relation
    ADD CONSTRAINT wx_user_group_relation_pkey PRIMARY KEY (id);


--
-- Name: wx_user_phone_key; Type: CONSTRAINT; Schema: public; Owner: wxshop
--

ALTER TABLE ONLY public.wx_user
    ADD CONSTRAINT wx_user_phone_key UNIQUE (phone);


--
-- Name: wx_user_pkey; Type: CONSTRAINT; Schema: public; Owner: wxshop
--

ALTER TABLE ONLY public.wx_user
    ADD CONSTRAINT wx_user_pkey PRIMARY KEY (id);


--
-- Name: wx_user_username_key; Type: CONSTRAINT; Schema: public; Owner: wxshop
--

ALTER TABLE ONLY public.wx_user
    ADD CONSTRAINT wx_user_username_key UNIQUE (username);
