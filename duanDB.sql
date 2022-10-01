PGDMP     '    (                z            duanDB    13.2    13.2 �   �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    82343    duanDB    DATABASE     l   CREATE DATABASE "duanDB" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'English_United States.1252';
    DROP DATABASE "duanDB";
                postgres    false                        3079    82344    postgis 	   EXTENSION     ;   CREATE EXTENSION IF NOT EXISTS postgis WITH SCHEMA public;
    DROP EXTENSION postgis;
                   false            �           0    0    EXTENSION postgis    COMMENT     g   COMMENT ON EXTENSION postgis IS 'PostGIS geometry, geography, and raster spatial types and functions';
                        false    2            w           1259    85519 
   auth_group    TABLE     f   CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);
    DROP TABLE public.auth_group;
       public         heap    postgres    false            v           1259    85517    auth_group_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.auth_group_id_seq;
       public          postgres    false    375            �           0    0    auth_group_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;
          public          postgres    false    374            y           1259    85529    auth_group_permissions    TABLE     �   CREATE TABLE public.auth_group_permissions (
    id bigint NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);
 *   DROP TABLE public.auth_group_permissions;
       public         heap    postgres    false            x           1259    85527    auth_group_permissions_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE public.auth_group_permissions_id_seq;
       public          postgres    false    377            �           0    0    auth_group_permissions_id_seq    SEQUENCE OWNED BY     _   ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;
          public          postgres    false    376            �            1259    83376    auth_permission    TABLE     �   CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    codename character varying(100) NOT NULL,
    content_type_id integer NOT NULL
);
 #   DROP TABLE public.auth_permission;
       public         heap    postgres    false            �            1259    83374    auth_permission_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.auth_permission_id_seq;
       public          postgres    false    211            �           0    0    auth_permission_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;
          public          postgres    false    210            �            1259    83651 (   biengioidiagioi_diaphanhanhchinhtrenbien    TABLE       CREATE TABLE public.biengioidiagioi_diaphanhanhchinhtrenbien (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    madoituong character varying(50) NOT NULL,
    madonvihanhchinh character varying(20) NOT NULL,
    ten character varying(255) NOT NULL,
    dientich double precision,
    gm_surface public.geometry(Polygon,4756) NOT NULL
);
 <   DROP TABLE public.biengioidiagioi_diaphanhanhchinhtrenbien;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            �            1259    83659 +   biengioidiagioi_diaphanhanhchinhtrendatlien    TABLE     4  CREATE TABLE public.biengioidiagioi_diaphanhanhchinhtrendatlien (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    "maDonViHanhChinh" character varying(50) NOT NULL,
    ten character varying(50) NOT NULL,
    "dienTich" double precision NOT NULL,
    "soDan" integer NOT NULL,
    "GM_Surface" public.geometry(Polygon,4756) NOT NULL
);
 ?   DROP TABLE public.biengioidiagioi_diaphanhanhchinhtrendatlien;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            �            1259    83667 .   biengioidiagioi_duongranhgioihanhchinhtrenbien    TABLE     �  CREATE TABLE public.biengioidiagioi_duongranhgioihanhchinhtrenbien (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    "loaiHienTrangPhapLy" integer NOT NULL,
    "chieuDai" double precision NOT NULL,
    "GM_Curve" public.geometry(LineString,4756) NOT NULL
);
 B   DROP TABLE public.biengioidiagioi_duongranhgioihanhchinhtrenbien;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            �            1259    83675    biengioidiagioi_vungbien    TABLE     �  CREATE TABLE public.biengioidiagioi_vungbien (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    "dienTich" double precision,
    "GM_Surface" public.geometry(Polygon,4756) NOT NULL
);
 ,   DROP TABLE public.biengioidiagioi_vungbien;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            �            1259    83691    cosododac_diemdodacquocgia    TABLE       CREATE TABLE public.cosododac_diemdodacquocgia (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "soHieuDiem" character varying(50) NOT NULL,
    "GM_Point" public.geometry(Point,4756) NOT NULL,
    "maDoiTuong" character varying(50) NOT NULL,
    "doCao" double precision NOT NULL,
    "loaiMoc" integer NOT NULL,
    "loaiCapHang" integer NOT NULL
);
 .   DROP TABLE public.cosododac_diemdodacquocgia;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            �            1259    83699    cosododac_diemgocdodacquocgia    TABLE     �  CREATE TABLE public.cosododac_diemgocdodacquocgia (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "soHieuDiem" character varying(50) NOT NULL,
    "GM_Point" public.geometry(Point,4756) NOT NULL,
    "maDoiTuong" character varying(50) NOT NULL,
    "doCao" double precision NOT NULL
);
 1   DROP TABLE public.cosododac_diemgocdodacquocgia;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            �            1259    83707 !   cosododac_tramdinhvivetinhquocgia    TABLE       CREATE TABLE public.cosododac_tramdinhvivetinhquocgia (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "soHieuDiem" character varying(50) NOT NULL,
    "GM_Point" public.geometry(Point,4756) NOT NULL,
    "maDoiTuong" character varying(50) NOT NULL,
    ten character varying(255) NOT NULL,
    "loaiTramDinhViVeTinh" integer NOT NULL
);
 5   DROP TABLE public.cosododac_tramdinhvivetinhquocgia;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            �            1259    83721    dancu_congtrinhcongnghiep    TABLE     �  CREATE TABLE public.dancu_congtrinhcongnghiep (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    ten character varying(255),
    "loaiCongTrinhCongNghiep" integer NOT NULL
);
 -   DROP TABLE public.dancu_congtrinhcongnghiep;
       public         heap    postgres    false            �            1259    83729    dancu_cotdien    TABLE     k  CREATE TABLE public.dancu_cotdien (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    "GM_Point" public.geometry(Point,4756) NOT NULL
);
 !   DROP TABLE public.dancu_cotdien;
       public         heap    postgres    false    2    2    2    2    2    2    2    2                       1259    84041    dancu_curve_congtrinhcongnghiep    TABLE     �   CREATE TABLE public.dancu_curve_congtrinhcongnghiep (
    congtrinhcongnghiep_ptr_id character varying(50) NOT NULL,
    "GM_Curve" public.geometry(LineString,4756) NOT NULL
);
 3   DROP TABLE public.dancu_curve_congtrinhcongnghiep;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            �            1259    83737    dancu_curve_congtrinhphutro    TABLE     ~  CREATE TABLE public.dancu_curve_congtrinhphutro (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    "GM_Curve" public.geometry(LineString,4756) NOT NULL
);
 /   DROP TABLE public.dancu_curve_congtrinhphutro;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            �            1259    83745    dancu_diadanhdancu    TABLE     �  CREATE TABLE public.dancu_diadanhdancu (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    "danhTuChung" integer NOT NULL,
    ten character varying(255),
    "GM_Point" public.geometry(Point,4756) NOT NULL
);
 &   DROP TABLE public.dancu_diadanhdancu;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            �            1259    83753    dancu_duongdaytaidien    TABLE     �  CREATE TABLE public.dancu_duongdaytaidien (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    "dienAp" double precision NOT NULL,
    "GM_Curve" public.geometry(LineString,4756) NOT NULL
);
 )   DROP TABLE public.dancu_duongdaytaidien;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            �            1259    83761    dancu_duongongdan    TABLE     �  CREATE TABLE public.dancu_duongongdan (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    "loaiOngDan" integer NOT NULL,
    "GM_Curve" public.geometry(LineString,4756) NOT NULL
);
 %   DROP TABLE public.dancu_duongongdan;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            �            1259    83769    dancu_khoinha    TABLE     �  CREATE TABLE public.dancu_khoinha (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    "nhomSoTang" integer NOT NULL,
    "nhomChieuCao" integer NOT NULL,
    "GM_Surface" public.geometry(Polygon,4756) NOT NULL
);
 !   DROP TABLE public.dancu_khoinha;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            �            1259    83777    dancu_khuchucnangdacthu    TABLE     �  CREATE TABLE public.dancu_khuchucnangdacthu (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    ten character varying(255),
    "GM_Surface" public.geometry(Polygon,4756) NOT NULL
);
 +   DROP TABLE public.dancu_khuchucnangdacthu;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            �            1259    83785    dancu_khudancu    TABLE     �  CREATE TABLE public.dancu_khudancu (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    "loaiKhuDanCu" integer NOT NULL,
    "soDan" integer,
    ten character varying(255),
    "GM_Surface" public.geometry(Polygon,4756) NOT NULL
);
 "   DROP TABLE public.dancu_khudancu;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            �            1259    83793    dancu_point_congtrinhanninh    TABLE     �  CREATE TABLE public.dancu_point_congtrinhanninh (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    ten character varying(255),
    "GM_Point" public.geometry(Point,4756) NOT NULL
);
 /   DROP TABLE public.dancu_point_congtrinhanninh;
       public         heap    postgres    false    2    2    2    2    2    2    2    2                       1259    84049    dancu_point_congtrinhcongnghiep    TABLE     �   CREATE TABLE public.dancu_point_congtrinhcongnghiep (
    congtrinhcongnghiep_ptr_id character varying(50) NOT NULL,
    "GM_Point" public.geometry(Point,4756) NOT NULL
);
 3   DROP TABLE public.dancu_point_congtrinhcongnghiep;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            �            1259    83801    dancu_point_congtrinhgiaoduc    TABLE     �  CREATE TABLE public.dancu_point_congtrinhgiaoduc (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    ten character varying(255),
    "GM_Point" public.geometry(Point,4756) NOT NULL
);
 0   DROP TABLE public.dancu_point_congtrinhgiaoduc;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            �            1259    83809    dancu_point_congtrinhquocphong    TABLE     �  CREATE TABLE public.dancu_point_congtrinhquocphong (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    ten character varying(255),
    "GM_Point" public.geometry(Point,4756) NOT NULL
);
 2   DROP TABLE public.dancu_point_congtrinhquocphong;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            �            1259    83817    dancu_point_congtrinhthethao    TABLE     �  CREATE TABLE public.dancu_point_congtrinhthethao (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    ten character varying(255),
    "GM_Point" public.geometry(Point,4756) NOT NULL
);
 0   DROP TABLE public.dancu_point_congtrinhthethao;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            �            1259    83825 $   dancu_point_congtrinhthuongmaidichvu    TABLE     �  CREATE TABLE public.dancu_point_congtrinhthuongmaidichvu (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    ten character varying(255),
    "GM_Point" public.geometry(Point,4756) NOT NULL
);
 8   DROP TABLE public.dancu_point_congtrinhthuongmaidichvu;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            �            1259    83833 %   dancu_point_congtrinhtongiaotinnguong    TABLE     �  CREATE TABLE public.dancu_point_congtrinhtongiaotinnguong (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    ten character varying(255),
    "xepHangDiTich" integer NOT NULL,
    "GM_Point" public.geometry(Point,4756) NOT NULL
);
 9   DROP TABLE public.dancu_point_congtrinhtongiaotinnguong;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            �            1259    83841    dancu_point_congtrinhvanhoa    TABLE     �  CREATE TABLE public.dancu_point_congtrinhvanhoa (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    ten character varying(255),
    "xepHangDiTich" integer NOT NULL,
    "chieuCao" double precision,
    "GM_Point" public.geometry(Point,4756) NOT NULL
);
 /   DROP TABLE public.dancu_point_congtrinhvanhoa;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            �            1259    83849 !   dancu_point_congtrinhxulychatthai    TABLE     �  CREATE TABLE public.dancu_point_congtrinhxulychatthai (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    ten character varying(255),
    "GM_Point" public.geometry(Point,4756) NOT NULL
);
 5   DROP TABLE public.dancu_point_congtrinhxulychatthai;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            �            1259    83857    dancu_point_congtrinhyte    TABLE     �  CREATE TABLE public.dancu_point_congtrinhyte (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    "capYTe" integer NOT NULL,
    ten character varying(255),
    "GM_Point" public.geometry(Point,4756) NOT NULL
);
 ,   DROP TABLE public.dancu_point_congtrinhyte;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            �            1259    83865 $   dancu_point_cososanxuatnonglamnghiep    TABLE     �  CREATE TABLE public.dancu_point_cososanxuatnonglamnghiep (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    ten character varying(255),
    "GM_Point" public.geometry(Point,4756) NOT NULL
);
 8   DROP TABLE public.dancu_point_cososanxuatnonglamnghiep;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            �            1259    83873    dancu_point_hatangkythuatkhac    TABLE     �  CREATE TABLE public.dancu_point_hatangkythuatkhac (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    ten character varying(255),
    "chieuCao" double precision,
    "GM_Point" public.geometry(Point,4756) NOT NULL
);
 1   DROP TABLE public.dancu_point_hatangkythuatkhac;
       public         heap    postgres    false    2    2    2    2    2    2    2    2                        1259    83881    dancu_point_nha    TABLE     ?  CREATE TABLE public.dancu_point_nha (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    "loaiNha" integer NOT NULL,
    "mucDoKienCo" integer NOT NULL,
    "chieuCao" double precision NOT NULL,
    "soTang" integer NOT NULL,
    ten character varying(255),
    "diaChi" character varying(255),
    "GM_Point" public.geometry(Point,4756) NOT NULL
);
 #   DROP TABLE public.dancu_point_nha;
       public         heap    postgres    false    2    2    2    2    2    2    2    2                       1259    83889    dancu_point_trusocoquannhanuoc    TABLE     �  CREATE TABLE public.dancu_point_trusocoquannhanuoc (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    ten character varying(255),
    "GM_Point" public.geometry(Point,4756) NOT NULL
);
 2   DROP TABLE public.dancu_point_trusocoquannhanuoc;
       public         heap    postgres    false    2    2    2    2    2    2    2    2                       1259    83897    dancu_ranhgioi    TABLE     �  CREATE TABLE public.dancu_ranhgioi (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    "loaiRanhGioi" integer NOT NULL,
    "GM_Curve" public.geometry(LineString,4756) NOT NULL
);
 "   DROP TABLE public.dancu_ranhgioi;
       public         heap    postgres    false    2    2    2    2    2    2    2    2                       1259    83905    dancu_surface_congtrinhanninh    TABLE     �  CREATE TABLE public.dancu_surface_congtrinhanninh (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    ten character varying(255),
    "GM_Surface" public.geometry(Polygon,4756) NOT NULL
);
 1   DROP TABLE public.dancu_surface_congtrinhanninh;
       public         heap    postgres    false    2    2    2    2    2    2    2    2                       1259    84057 !   dancu_surface_congtrinhcongnghiep    TABLE     �   CREATE TABLE public.dancu_surface_congtrinhcongnghiep (
    congtrinhcongnghiep_ptr_id character varying(50) NOT NULL,
    "GM_Surface" public.geometry(Polygon,4756) NOT NULL
);
 5   DROP TABLE public.dancu_surface_congtrinhcongnghiep;
       public         heap    postgres    false    2    2    2    2    2    2    2    2                       1259    83913    dancu_surface_congtrinhgiaoduc    TABLE     �  CREATE TABLE public.dancu_surface_congtrinhgiaoduc (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    ten character varying(255),
    "GM_Surface" public.geometry(Polygon,4756) NOT NULL
);
 2   DROP TABLE public.dancu_surface_congtrinhgiaoduc;
       public         heap    postgres    false    2    2    2    2    2    2    2    2                       1259    83921    dancu_surface_congtrinhphutro    TABLE       CREATE TABLE public.dancu_surface_congtrinhphutro (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    "GM_Surface" public.geometry(Polygon,4756) NOT NULL
);
 1   DROP TABLE public.dancu_surface_congtrinhphutro;
       public         heap    postgres    false    2    2    2    2    2    2    2    2                       1259    83929     dancu_surface_congtrinhquocphong    TABLE     �  CREATE TABLE public.dancu_surface_congtrinhquocphong (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    ten character varying(255),
    "GM_Surface" public.geometry(Polygon,4756) NOT NULL
);
 4   DROP TABLE public.dancu_surface_congtrinhquocphong;
       public         heap    postgres    false    2    2    2    2    2    2    2    2                       1259    83937    dancu_surface_congtrinhthethao    TABLE     �  CREATE TABLE public.dancu_surface_congtrinhthethao (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    ten character varying(255),
    "GM_Surface" public.geometry(Polygon,4756) NOT NULL
);
 2   DROP TABLE public.dancu_surface_congtrinhthethao;
       public         heap    postgres    false    2    2    2    2    2    2    2    2                       1259    83945 &   dancu_surface_congtrinhthuongmaidichvu    TABLE     �  CREATE TABLE public.dancu_surface_congtrinhthuongmaidichvu (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    ten character varying(255),
    "GM_Surface" public.geometry(Polygon,4756) NOT NULL
);
 :   DROP TABLE public.dancu_surface_congtrinhthuongmaidichvu;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            	           1259    83953 '   dancu_surface_congtrinhtongiaotinnguong    TABLE     �  CREATE TABLE public.dancu_surface_congtrinhtongiaotinnguong (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    ten character varying(255),
    "xepHangDiTich" integer NOT NULL,
    "GM_Surface" public.geometry(Polygon,4756) NOT NULL
);
 ;   DROP TABLE public.dancu_surface_congtrinhtongiaotinnguong;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            
           1259    83961    dancu_surface_congtrinhvanhoa    TABLE     �  CREATE TABLE public.dancu_surface_congtrinhvanhoa (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    ten character varying(255),
    "xepHangDiTich" integer NOT NULL,
    "chieuCao" double precision,
    "GM_Surface" public.geometry(Polygon,4756) NOT NULL
);
 1   DROP TABLE public.dancu_surface_congtrinhvanhoa;
       public         heap    postgres    false    2    2    2    2    2    2    2    2                       1259    83969 #   dancu_surface_congtrinhxulychatthai    TABLE     �  CREATE TABLE public.dancu_surface_congtrinhxulychatthai (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    ten character varying(255),
    "GM_Surface" public.geometry(Polygon,4756) NOT NULL
);
 7   DROP TABLE public.dancu_surface_congtrinhxulychatthai;
       public         heap    postgres    false    2    2    2    2    2    2    2    2                       1259    83977    dancu_surface_congtrinhyte    TABLE     �  CREATE TABLE public.dancu_surface_congtrinhyte (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    "capYTe" integer NOT NULL,
    ten character varying(255),
    "GM_Surface" public.geometry(Polygon,4756) NOT NULL
);
 .   DROP TABLE public.dancu_surface_congtrinhyte;
       public         heap    postgres    false    2    2    2    2    2    2    2    2                       1259    83985 &   dancu_surface_cososanxuatnonglamnghiep    TABLE     �  CREATE TABLE public.dancu_surface_cososanxuatnonglamnghiep (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    ten character varying(255),
    "GM_Surface" public.geometry(Polygon,4756) NOT NULL
);
 :   DROP TABLE public.dancu_surface_cososanxuatnonglamnghiep;
       public         heap    postgres    false    2    2    2    2    2    2    2    2                       1259    83993    dancu_surface_hatangkythuatkhac    TABLE     �  CREATE TABLE public.dancu_surface_hatangkythuatkhac (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    ten character varying(255),
    "chieuCao" double precision,
    "GM_Surface" public.geometry(Polygon,4756) NOT NULL
);
 3   DROP TABLE public.dancu_surface_hatangkythuatkhac;
       public         heap    postgres    false    2    2    2    2    2    2    2    2                       1259    84001    dancu_surface_nha    TABLE     E  CREATE TABLE public.dancu_surface_nha (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    "loaiNha" integer NOT NULL,
    "mucDoKienCo" integer NOT NULL,
    "chieuCao" double precision NOT NULL,
    "soTang" integer NOT NULL,
    ten character varying(255),
    "diaChi" character varying(255),
    "GM_Surface" public.geometry(Polygon,4756) NOT NULL
);
 %   DROP TABLE public.dancu_surface_nha;
       public         heap    postgres    false    2    2    2    2    2    2    2    2                       1259    84009     dancu_surface_trusocoquannhanuoc    TABLE     �  CREATE TABLE public.dancu_surface_trusocoquannhanuoc (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    ten character varying(255),
    "GM_Surface" public.geometry(Polygon,4756) NOT NULL
);
 4   DROP TABLE public.dancu_surface_trusocoquannhanuoc;
       public         heap    postgres    false    2    2    2    2    2    2    2    2                       1259    84017     dancu_tramkhituongthuyvanquocgia    TABLE     �  CREATE TABLE public.dancu_tramkhituongthuyvanquocgia (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    "loaiTramKhiTuongThuyVan" integer NOT NULL,
    ten character varying(255),
    "GM_Surface" public.geometry(Polygon,4756) NOT NULL
);
 4   DROP TABLE public.dancu_tramkhituongthuyvanquocgia;
       public         heap    postgres    false    2    2    2    2    2    2    2    2                       1259    84025    dancu_tramquantracmoitruong    TABLE     �  CREATE TABLE public.dancu_tramquantracmoitruong (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    ten character varying(255),
    "GM_Surface" public.geometry(Polygon,4756) NOT NULL
);
 /   DROP TABLE public.dancu_tramquantracmoitruong;
       public         heap    postgres    false    2    2    2    2    2    2    2    2                       1259    84033    dancu_tramquantractainguyennuoc    TABLE     �  CREATE TABLE public.dancu_tramquantractainguyennuoc (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    ten character varying(255),
    "GM_Surface" public.geometry(Polygon,4756) NOT NULL
);
 3   DROP TABLE public.dancu_tramquantractainguyennuoc;
       public         heap    postgres    false    2    2    2    2    2    2    2    2                       1259    84165    diahinh_chatday    TABLE     �  CREATE TABLE public.diahinh_chatday (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    "loaiChatDay" integer NOT NULL,
    "GM_Point" public.geometry(Point,4756) NOT NULL
);
 #   DROP TABLE public.diahinh_chatday;
       public         heap    postgres    false    2    2    2    2    2    2    2    2                       1259    84173 #   diahinh_curve_diahinhdacbietdaybien    TABLE     �  CREATE TABLE public.diahinh_curve_diahinhdacbietdaybien (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    "GM_Curve" public.geometry(LineString,4756) NOT NULL
);
 7   DROP TABLE public.diahinh_curve_diahinhdacbietdaybien;
       public         heap    postgres    false    2    2    2    2    2    2    2    2                       1259    84181    diahinh_diamao    TABLE     V  CREATE TABLE public.diahinh_diamao (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    "tenDiaMao" character varying(255) NOT NULL,
    "dongLucDiaMao" character varying(255) NOT NULL,
    "motaDiaMao" character varying(255),
    "tyleDiaMao" double precision NOT NULL,
    "ghichuDiaMao" character varying(500),
    "GM_Surface" public.geometry(Polygon,4756) NOT NULL
);
 "   DROP TABLE public.diahinh_diamao;
       public         heap    postgres    false    2    2    2    2    2    2    2    2                       1259    84189    diahinh_diemdocao    TABLE     �  CREATE TABLE public.diahinh_diemdocao (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    "doCao" double precision NOT NULL,
    "GM_Point" public.geometry(Point,4756) NOT NULL
);
 %   DROP TABLE public.diahinh_diemdocao;
       public         heap    postgres    false    2    2    2    2    2    2    2    2                       1259    84197    diahinh_diemdosau    TABLE     �  CREATE TABLE public.diahinh_diemdosau (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    "doSau" double precision NOT NULL,
    "GM_Point" public.geometry(Point,4756) NOT NULL
);
 %   DROP TABLE public.diahinh_diemdosau;
       public         heap    postgres    false    2    2    2    2    2    2    2    2                       1259    84205    diahinh_duongbinhdo    TABLE     �  CREATE TABLE public.diahinh_duongbinhdo (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    "loaiDuongBinhDo" integer NOT NULL,
    "loaiKhoangCaoDeu" integer NOT NULL,
    "doCao" double precision NOT NULL,
    "GM_Curve" public.geometry(LineString,4756) NOT NULL
);
 '   DROP TABLE public.diahinh_duongbinhdo;
       public         heap    postgres    false    2    2    2    2    2    2    2    2                       1259    84213    diahinh_duongbinhdosau    TABLE     �  CREATE TABLE public.diahinh_duongbinhdosau (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    "loaiDuongBinhDo" integer NOT NULL,
    "loaiKhoangCaoDeu" integer NOT NULL,
    "doSau" double precision NOT NULL,
    "GM_Curve" public.geometry(LineString,4756) NOT NULL
);
 *   DROP TABLE public.diahinh_duongbinhdosau;
       public         heap    postgres    false    2    2    2    2    2    2    2    2                       1259    84221    diahinh_hokhoandiachat    TABLE     F  CREATE TABLE public.diahinh_hokhoandiachat (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    "tenHoKhoanDiaChat" character varying(255) NOT NULL,
    "motaHoKhoanDiaChat" character varying(500),
    "dosauHoKhoanDiaChat" double precision NOT NULL,
    "ghichuHoKhoanDiaChat" character varying(500),
    "GM_Point" public.geometry(Point,4756) NOT NULL
);
 *   DROP TABLE public.diahinh_hokhoandiachat;
       public         heap    postgres    false    2    2    2    2    2    2    2    2                       1259    84229    diahinh_loaidiachat    TABLE     �  CREATE TABLE public.diahinh_loaidiachat (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    "phanHeThachHoc" character varying(255) NOT NULL,
    "kieuThachHoc" character varying(255) NOT NULL,
    "kieuDiaChatCongTrinh" character varying(255) NOT NULL,
    "tuoiDiaChatCongTrinh" double precision NOT NULL,
    "kyHieu" character varying(50),
    "moTa" character varying(500),
    "GM_Surface" public.geometry(Polygon,4756) NOT NULL
);
 '   DROP TABLE public.diahinh_loaidiachat;
       public         heap    postgres    false    2    2    2    2    2    2    2    2                        1259    84237    diahinh_matcatdienhinh    TABLE     ?  CREATE TABLE public.diahinh_matcatdienhinh (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    ten character varying(255),
    "moTa" character varying(500) NOT NULL,
    "tyLeDung" double precision NOT NULL,
    "tyLeNgang" double precision NOT NULL,
    "ghiChu" character varying(500),
    "GM_Curve" public.geometry(LineString,4756) NOT NULL
);
 *   DROP TABLE public.diahinh_matcatdienhinh;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            !           1259    84245    diahinh_mohinhsodocaogoclopdiem    TABLE     }  CREATE TABLE public.diahinh_mohinhsodocaogoclopdiem (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    "GM_Point" public.geometry(Point,4756) NOT NULL
);
 3   DROP TABLE public.diahinh_mohinhsodocaogoclopdiem;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            "           1259    84253     diahinh_mohinhsodocaogoclopduong    TABLE     �  CREATE TABLE public.diahinh_mohinhsodocaogoclopduong (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    "GM_Curve" public.geometry(LineString,4756) NOT NULL
);
 4   DROP TABLE public.diahinh_mohinhsodocaogoclopduong;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            #           1259    84261    diahinh_mohinhsodocaogoclopvung    TABLE     �  CREATE TABLE public.diahinh_mohinhsodocaogoclopvung (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    "GM_Surface" public.geometry(Polygon,4756) NOT NULL
);
 3   DROP TABLE public.diahinh_mohinhsodocaogoclopvung;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            $           1259    84269 &   diahinh_mohinhsodocaogoclopvungbientap    TABLE     �  CREATE TABLE public.diahinh_mohinhsodocaogoclopvungbientap (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    "GM_Surface" public.geometry(Polygon,4756) NOT NULL
);
 :   DROP TABLE public.diahinh_mohinhsodocaogoclopvungbientap;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            '           1259    84287    diahinh_solieuhkdc    TABLE     �  CREATE TABLE public.diahinh_solieuhkdc (
    id bigint NOT NULL,
    "maSolieuHoKhoanDC" character varying(50) NOT NULL,
    "dosauBDLaymauHKDC" double precision NOT NULL,
    "dosauKTLaymauHKDC" double precision NOT NULL,
    "soHieuMau" character varying(500) NOT NULL,
    "sohieuTNghiemHKDC" character varying(500) NOT NULL,
    "lopHKDC" character varying(500) NOT NULL,
    "P10" double precision,
    "P5" double precision,
    "P2" double precision,
    "P1" double precision,
    "P0_5" double precision,
    "P0_25" double precision,
    "P0_1" double precision,
    "P0_05" double precision,
    "P0_01" double precision,
    "P0_005" double precision,
    "DoAmTuNhien" double precision,
    "KLTheTichTuNhien" double precision,
    "KLTheTichKho" double precision,
    "KLRieng" double precision,
    "HeSoRong" double precision,
    "DoLoRong" double precision,
    "DoBaoHoa" double precision,
    "GocNghiKho" double precision,
    "GocNghiUot" double precision,
    "HSRongLonNhat" double precision,
    "HSRongNhoNhat" double precision,
    "DungTrongMaxCat" double precision,
    "DungTrongMinCat" double precision,
    "CDKNKho" double precision,
    "CDKNBaoHoa" double precision,
    "CDKNHeSoMem" double precision,
    "TinhCoLyDa_KLTTTN" double precision,
    "TinhCoLyDa_DoRong" double precision,
    "TinhCoLyDa_TyLeKheHo" double precision,
    "TinhCoLyDa_DoKheHo" double precision,
    "TinhCoLyDa_KLRieng" double precision,
    "TNNenDa_Kho" double precision,
    "TNNenDa_BaoHoa" double precision,
    "TNNenDa_HeSoHM" double precision,
    "R0" double precision,
    "E0" double precision,
    "Phanloaidat_HKDC" double precision,
    "HKDC_id" character varying(50) NOT NULL
);
 &   DROP TABLE public.diahinh_solieuhkdc;
       public         heap    postgres    false            &           1259    84285    diahinh_solieuhkdc_id_seq    SEQUENCE     �   CREATE SEQUENCE public.diahinh_solieuhkdc_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 0   DROP SEQUENCE public.diahinh_solieuhkdc_id_seq;
       public          postgres    false    295            �           0    0    diahinh_solieuhkdc_id_seq    SEQUENCE OWNED BY     W   ALTER SEQUENCE public.diahinh_solieuhkdc_id_seq OWNED BY public.diahinh_solieuhkdc.id;
          public          postgres    false    294            %           1259    84277 %   diahinh_surface_diahinhdacbietdaybien    TABLE     �  CREATE TABLE public.diahinh_surface_diahinhdacbietdaybien (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    "GM_Surface" public.geometry(Polygon,4756) NOT NULL
);
 9   DROP TABLE public.diahinh_surface_diahinhdacbietdaybien;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            �            1259    83627    django_admin_log    TABLE     �  CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id bigint NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);
 $   DROP TABLE public.django_admin_log;
       public         heap    postgres    false            �            1259    83625    django_admin_log_id_seq    SEQUENCE     �   CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.django_admin_log_id_seq;
       public          postgres    false    228            �           0    0    django_admin_log_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;
          public          postgres    false    227            �            1259    83366    django_content_type    TABLE     �   CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);
 '   DROP TABLE public.django_content_type;
       public         heap    postgres    false            �            1259    83364    django_content_type_id_seq    SEQUENCE     �   CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.django_content_type_id_seq;
       public          postgres    false    209            �           0    0    django_content_type_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;
          public          postgres    false    208            �            1259    83355    django_migrations    TABLE     �   CREATE TABLE public.django_migrations (
    id bigint NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);
 %   DROP TABLE public.django_migrations;
       public         heap    postgres    false            �            1259    83353    django_migrations_id_seq    SEQUENCE     �   CREATE SEQUENCE public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.django_migrations_id_seq;
       public          postgres    false    207            �           0    0    django_migrations_id_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;
          public          postgres    false    206            O           1259    84745    django_session    TABLE     �   CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);
 "   DROP TABLE public.django_session;
       public         heap    postgres    false            �            1259    83388    dulieuquantri_bienchetrangbi    TABLE     "  CREATE TABLE public.dulieuquantri_bienchetrangbi (
    "maNhanDang" character varying(20) NOT NULL,
    "tenTrangBi" character varying(50) NOT NULL,
    "donViTinh" character varying(20) NOT NULL,
    "soLuong" integer NOT NULL,
    "soHieuTrangBi" character varying(30),
    "phanCapChatLuong" integer NOT NULL,
    "phanBoTrangBi" integer NOT NULL,
    "deNghi" character varying(50),
    "chucNangTrangBi" character varying(100),
    link character varying(100),
    "ghiChu" text,
    "donVi_id" character varying(20) NOT NULL,
    "loaiTrangBiKhiTai_id" character varying(20) NOT NULL,
    "tinhTrangTrangBi_id" character varying(20),
    "xuatXu_id" character varying(20) NOT NULL,
    "namSanXuat" integer,
    CONSTRAINT "dulieuquantri_bienchetrangbi_soLuong_check" CHECK (("soLuong" >= 0))
);
 0   DROP TABLE public.dulieuquantri_bienchetrangbi;
       public         heap    postgres    false            �            1259    83397    dulieuquantri_capdonvi    TABLE     �   CREATE TABLE public.dulieuquantri_capdonvi (
    "maNhanDang" character varying(20) NOT NULL,
    "tenCap" character varying(100) NOT NULL,
    "KHQS" character varying(100),
    "ghiChu" text
);
 *   DROP TABLE public.dulieuquantri_capdonvi;
       public         heap    postgres    false            �            1259    83474    dulieuquantri_donvi    TABLE     �  CREATE TABLE public.dulieuquantri_donvi (
    "maNhanDang" character varying(20) NOT NULL,
    "tenDonVi" character varying(100) NOT NULL,
    "phienHieuDonVi" character varying(20),
    "diaChiDonVi" character varying(100),
    "sdtQSDonVi" character varying(12),
    "emailDonVi" character varying(30),
    "chucNangDonVi" character varying(100),
    "nhiemVuDonVi" character varying(100),
    "chiHuyTruongDonVi" character varying(30),
    "tongQSDonVi" integer NOT NULL,
    "ghiChu" text,
    "capDonVi_id" character varying(20),
    "loaiDonVi_id" character varying(20),
    "CTQP_id" character varying(50),
    CONSTRAINT "dulieuquantri_donvi_tongQSDonVi_check" CHECK (("tongQSDonVi" >= 0))
);
 '   DROP TABLE public.dulieuquantri_donvi;
       public         heap    postgres    false            �            1259    83423    dulieuquantri_loaidonvi    TABLE     �   CREATE TABLE public.dulieuquantri_loaidonvi (
    "maNhanDang" character varying(20) NOT NULL,
    "tenLoaiDonVi" character varying(50) NOT NULL,
    "ghiChu" text
);
 +   DROP TABLE public.dulieuquantri_loaidonvi;
       public         heap    postgres    false            �            1259    83431    dulieuquantri_loaitrangbikhitai    TABLE     �   CREATE TABLE public.dulieuquantri_loaitrangbikhitai (
    "maNhanDang" character varying(20) NOT NULL,
    "tenLoaiTrangBi" character varying(50) NOT NULL,
    "ghiChu" text
);
 3   DROP TABLE public.dulieuquantri_loaitrangbikhitai;
       public         heap    postgres    false            �            1259    83505    dulieuquantri_nguoidung    TABLE     9  CREATE TABLE public.dulieuquantri_nguoidung (
    id bigint NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL,
    anhdaidien character varying(100),
    "donVi_id" character varying(20)
);
 +   DROP TABLE public.dulieuquantri_nguoidung;
       public         heap    postgres    false            �            1259    83518    dulieuquantri_nguoidung_groups    TABLE     �   CREATE TABLE public.dulieuquantri_nguoidung_groups (
    id bigint NOT NULL,
    nguoidung_id bigint NOT NULL,
    group_id integer NOT NULL
);
 2   DROP TABLE public.dulieuquantri_nguoidung_groups;
       public         heap    postgres    false            �            1259    83516 %   dulieuquantri_nguoidung_groups_id_seq    SEQUENCE     �   CREATE SEQUENCE public.dulieuquantri_nguoidung_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 <   DROP SEQUENCE public.dulieuquantri_nguoidung_groups_id_seq;
       public          postgres    false    224            �           0    0 %   dulieuquantri_nguoidung_groups_id_seq    SEQUENCE OWNED BY     o   ALTER SEQUENCE public.dulieuquantri_nguoidung_groups_id_seq OWNED BY public.dulieuquantri_nguoidung_groups.id;
          public          postgres    false    223            �            1259    83503    dulieuquantri_nguoidung_id_seq    SEQUENCE     �   CREATE SEQUENCE public.dulieuquantri_nguoidung_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 5   DROP SEQUENCE public.dulieuquantri_nguoidung_id_seq;
       public          postgres    false    222            �           0    0    dulieuquantri_nguoidung_id_seq    SEQUENCE OWNED BY     a   ALTER SEQUENCE public.dulieuquantri_nguoidung_id_seq OWNED BY public.dulieuquantri_nguoidung.id;
          public          postgres    false    221            �            1259    83526 (   dulieuquantri_nguoidung_user_permissions    TABLE     �   CREATE TABLE public.dulieuquantri_nguoidung_user_permissions (
    id bigint NOT NULL,
    nguoidung_id bigint NOT NULL,
    permission_id integer NOT NULL
);
 <   DROP TABLE public.dulieuquantri_nguoidung_user_permissions;
       public         heap    postgres    false            �            1259    83524 /   dulieuquantri_nguoidung_user_permissions_id_seq    SEQUENCE     �   CREATE SEQUENCE public.dulieuquantri_nguoidung_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 F   DROP SEQUENCE public.dulieuquantri_nguoidung_user_permissions_id_seq;
       public          postgres    false    226            �           0    0 /   dulieuquantri_nguoidung_user_permissions_id_seq    SEQUENCE OWNED BY     �   ALTER SEQUENCE public.dulieuquantri_nguoidung_user_permissions_id_seq OWNED BY public.dulieuquantri_nguoidung_user_permissions.id;
          public          postgres    false    225            �            1259    83463    dulieuquantri_nhomtaikhoan    TABLE     �   CREATE TABLE public.dulieuquantri_nhomtaikhoan (
    id bigint NOT NULL,
    "moTa" text,
    "ghiChu" text,
    group_id integer NOT NULL,
    role integer NOT NULL
);
 .   DROP TABLE public.dulieuquantri_nhomtaikhoan;
       public         heap    postgres    false            �            1259    83461 !   dulieuquantri_nhomtaikhoan_id_seq    SEQUENCE     �   CREATE SEQUENCE public.dulieuquantri_nhomtaikhoan_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 8   DROP SEQUENCE public.dulieuquantri_nhomtaikhoan_id_seq;
       public          postgres    false    219            �           0    0 !   dulieuquantri_nhomtaikhoan_id_seq    SEQUENCE OWNED BY     g   ALTER SEQUENCE public.dulieuquantri_nhomtaikhoan_id_seq OWNED BY public.dulieuquantri_nhomtaikhoan.id;
          public          postgres    false    218            |           1259    91827    dulieuquantri_thietbikhitai    TABLE     Z  CREATE TABLE public.dulieuquantri_thietbikhitai (
    "maNhanDang" character varying(20) NOT NULL,
    "tenPhuKien" character varying(50) NOT NULL,
    "donViTinh" character varying(20) NOT NULL,
    "soLuong" integer NOT NULL,
    "dongBo" boolean NOT NULL,
    "namSanXuat" integer NOT NULL,
    "phanCapChatLuong" integer NOT NULL,
    "bienCheTB_id" character varying(20),
    "loaiTrangBiKhiTai_id" character varying(20),
    "tinhTrangTrangBi_id" character varying(20),
    "xuatXu_id" character varying(20),
    CONSTRAINT "dulieuquantri_thietbikhitai_soLuong_check" CHECK (("soLuong" >= 0))
);
 /   DROP TABLE public.dulieuquantri_thietbikhitai;
       public         heap    postgres    false            �            1259    83439    dulieuquantri_tinhtrangtrangbi    TABLE     �   CREATE TABLE public.dulieuquantri_tinhtrangtrangbi (
    "maNhanDang" character varying(20) NOT NULL,
    "tenTinhTrangTB" character varying(50) NOT NULL,
    "ghiChu" text
);
 2   DROP TABLE public.dulieuquantri_tinhtrangtrangbi;
       public         heap    postgres    false            �            1259    83447    dulieuquantri_xuatxu    TABLE     �   CREATE TABLE public.dulieuquantri_xuatxu (
    "maNhanDang" character varying(20) NOT NULL,
    "tenXuatXu" character varying(50) NOT NULL,
    "ghiChu" text
);
 (   DROP TABLE public.dulieuquantri_xuatxu;
       public         heap    postgres    false            )           1259    84335    eav_attribute    TABLE     �  CREATE TABLE public.eav_attribute (
    id bigint NOT NULL,
    datatype character varying(6) NOT NULL,
    name character varying(100) NOT NULL,
    slug character varying(50) NOT NULL,
    required boolean NOT NULL,
    description character varying(256),
    display_order integer NOT NULL,
    modified timestamp with time zone NOT NULL,
    created timestamp with time zone NOT NULL,
    enum_group_id bigint,
    CONSTRAINT eav_attribute_display_order_check CHECK ((display_order >= 0))
);
 !   DROP TABLE public.eav_attribute;
       public         heap    postgres    false            +           1259    84346    eav_attribute_entity_ct    TABLE     �   CREATE TABLE public.eav_attribute_entity_ct (
    id bigint NOT NULL,
    attribute_id bigint NOT NULL,
    contenttype_id integer NOT NULL
);
 +   DROP TABLE public.eav_attribute_entity_ct;
       public         heap    postgres    false            *           1259    84344    eav_attribute_entity_ct_id_seq    SEQUENCE     �   CREATE SEQUENCE public.eav_attribute_entity_ct_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 5   DROP SEQUENCE public.eav_attribute_entity_ct_id_seq;
       public          postgres    false    299            �           0    0    eav_attribute_entity_ct_id_seq    SEQUENCE OWNED BY     a   ALTER SEQUENCE public.eav_attribute_entity_ct_id_seq OWNED BY public.eav_attribute_entity_ct.id;
          public          postgres    false    298            (           1259    84333    eav_attribute_id_seq    SEQUENCE     }   CREATE SEQUENCE public.eav_attribute_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public.eav_attribute_id_seq;
       public          postgres    false    297            �           0    0    eav_attribute_id_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE public.eav_attribute_id_seq OWNED BY public.eav_attribute.id;
          public          postgres    false    296            1           1259    84375    eav_enumgroup    TABLE     h   CREATE TABLE public.eav_enumgroup (
    id bigint NOT NULL,
    name character varying(100) NOT NULL
);
 !   DROP TABLE public.eav_enumgroup;
       public         heap    postgres    false            0           1259    84373    eav_enumgroup_id_seq    SEQUENCE     }   CREATE SEQUENCE public.eav_enumgroup_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public.eav_enumgroup_id_seq;
       public          postgres    false    305            �           0    0    eav_enumgroup_id_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE public.eav_enumgroup_id_seq OWNED BY public.eav_enumgroup.id;
          public          postgres    false    304            3           1259    84385    eav_enumgroup_values    TABLE     �   CREATE TABLE public.eav_enumgroup_values (
    id bigint NOT NULL,
    enumgroup_id bigint NOT NULL,
    enumvalue_id bigint NOT NULL
);
 (   DROP TABLE public.eav_enumgroup_values;
       public         heap    postgres    false            2           1259    84383    eav_enumgroup_values_id_seq    SEQUENCE     �   CREATE SEQUENCE public.eav_enumgroup_values_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 2   DROP SEQUENCE public.eav_enumgroup_values_id_seq;
       public          postgres    false    307            �           0    0    eav_enumgroup_values_id_seq    SEQUENCE OWNED BY     [   ALTER SEQUENCE public.eav_enumgroup_values_id_seq OWNED BY public.eav_enumgroup_values.id;
          public          postgres    false    306            -           1259    84354    eav_enumvalue    TABLE     h   CREATE TABLE public.eav_enumvalue (
    id bigint NOT NULL,
    value character varying(50) NOT NULL
);
 !   DROP TABLE public.eav_enumvalue;
       public         heap    postgres    false            ,           1259    84352    eav_enumvalue_id_seq    SEQUENCE     }   CREATE SEQUENCE public.eav_enumvalue_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public.eav_enumvalue_id_seq;
       public          postgres    false    301            �           0    0    eav_enumvalue_id_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE public.eav_enumvalue_id_seq OWNED BY public.eav_enumvalue.id;
          public          postgres    false    300            /           1259    84364 	   eav_value    TABLE     *  CREATE TABLE public.eav_value (
    id bigint NOT NULL,
    entity_id character varying(50),
    entity_uuid uuid,
    created timestamp with time zone NOT NULL,
    modified timestamp with time zone NOT NULL,
    value_bool boolean,
    value_csv text,
    value_date timestamp with time zone,
    value_float double precision,
    value_int bigint,
    value_text text,
    value_json jsonb,
    generic_value_id integer,
    attribute_id bigint NOT NULL,
    entity_ct_id integer NOT NULL,
    generic_value_ct_id integer,
    value_enum_id bigint
);
    DROP TABLE public.eav_value;
       public         heap    postgres    false            .           1259    84362    eav_value_id_seq    SEQUENCE     y   CREATE SEQUENCE public.eav_value_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.eav_value_id_seq;
       public          postgres    false    303            �           0    0    eav_value_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.eav_value_id_seq OWNED BY public.eav_value.id;
          public          postgres    false    302            4           1259    84452    giaothong_baidaptructhang    TABLE     �  CREATE TABLE public.giaothong_baidaptructhang (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    "viTriBaiDap" integer NOT NULL,
    ten character varying(255),
    "GM_Surface" public.geometry(Polygon,4756) NOT NULL
);
 -   DROP TABLE public.giaothong_baidaptructhang;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            5           1259    84460 )   giaothong_baohieudanluonghanghaiduongthuy    TABLE     0  CREATE TABLE public.giaothong_baohieudanluonghanghaiduongthuy (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    "coDen" boolean NOT NULL,
    "huongBaoHieu" integer NOT NULL,
    "hinhDang" integer NOT NULL,
    "mauSac" integer NOT NULL,
    "phoiHopMauSac" integer NOT NULL,
    "GM_Point" public.geometry(Point,4756) NOT NULL
);
 =   DROP TABLE public.giaothong_baohieudanluonghanghaiduongthuy;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            6           1259    84468    giaothong_baohieuhanghaiais    TABLE     �  CREATE TABLE public.giaothong_baohieuhanghaiais (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    ten character varying(255),
    "GM_Point" public.geometry(Point,4756) NOT NULL
);
 /   DROP TABLE public.giaothong_baohieuhanghaiais;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            7           1259    84476    giaothong_bencang    TABLE     �  CREATE TABLE public.giaothong_bencang (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    ten character varying(255),
    "GM_Surface" public.geometry(Polygon,4756) NOT NULL
);
 %   DROP TABLE public.giaothong_bencang;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            8           1259    84484    giaothong_curve_cautau    TABLE     �  CREATE TABLE public.giaothong_curve_cautau (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    "loaiCauTau" integer NOT NULL,
    "GM_Curve" public.geometry(LineString,4756) NOT NULL
);
 *   DROP TABLE public.giaothong_curve_cautau;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            9           1259    84492    giaothong_curve_conggiaothong    TABLE     �  CREATE TABLE public.giaothong_curve_conggiaothong (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    ten character varying(255),
    "GM_Curve" public.geometry(LineString,4756) NOT NULL
);
 1   DROP TABLE public.giaothong_curve_conggiaothong;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            :           1259    84500    giaothong_curve_nhomautau    TABLE     |  CREATE TABLE public.giaothong_curve_nhomautau (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    "GM_Curve" public.geometry(LineString,4756) NOT NULL
);
 -   DROP TABLE public.giaothong_curve_nhomautau;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            ;           1259    84508    giaothong_duongbang    TABLE     u  CREATE TABLE public.giaothong_duongbang (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    "GM_Surface" public.geometry(Polygon,4756) NOT NULL
);
 '   DROP TABLE public.giaothong_duongbang;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            <           1259    84516    giaothong_duongbo    TABLE     ;  CREATE TABLE public.giaothong_duongbo (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    "loaiDuongBo" integer NOT NULL,
    "capKyThuat" integer NOT NULL,
    "loaiChatLieuTraiMat" integer NOT NULL,
    "loaiHienTrangSuDung" integer NOT NULL,
    "chieuXeChay" integer NOT NULL,
    "viTri" integer NOT NULL,
    "soLanDuong" integer NOT NULL,
    "chieuRong" double precision NOT NULL,
    ten character varying(255) NOT NULL,
    "lienKetGiaoThong" integer NOT NULL,
    "tenTuyenGiaoThongXuyenQuocGia" character varying(255) NOT NULL,
    "tenQuocLo" character varying(255) NOT NULL,
    "tenDuongTinh" character varying(255) NOT NULL,
    "tenDuongHuyen" character varying(255) NOT NULL,
    "tenDuongXa" character varying(255) NOT NULL,
    "tenDuongDoThi" character varying(255) NOT NULL,
    "GM_Curve" public.geometry(LineString,4756) NOT NULL
);
 %   DROP TABLE public.giaothong_duongbo;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            =           1259    84524 (   giaothong_point_cacdoituonghanghaihaivan    TABLE     �  CREATE TABLE public.giaothong_point_cacdoituonghanghaihaivan (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    ten character varying(255),
    "GM_Point" public.geometry(Point,4756) NOT NULL
);
 <   DROP TABLE public.giaothong_point_cacdoituonghanghaihaivan;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            >           1259    84532    giaothong_point_conggiaothong    TABLE     �  CREATE TABLE public.giaothong_point_conggiaothong (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    ten character varying(255),
    "GM_Point" public.geometry(Point,4756) NOT NULL
);
 1   DROP TABLE public.giaothong_point_conggiaothong;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            ?           1259    84540 *   giaothong_surface_cacdoituonghanghaihaivan    TABLE     �  CREATE TABLE public.giaothong_surface_cacdoituonghanghaihaivan (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    ten character varying(255),
    "GM_Surface" public.geometry(Polygon,4756) NOT NULL
);
 >   DROP TABLE public.giaothong_surface_cacdoituonghanghaihaivan;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            @           1259    84548    giaothong_surface_cautau    TABLE     �  CREATE TABLE public.giaothong_surface_cautau (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    "loaiCauTau" integer NOT NULL,
    "GM_Surface" public.geometry(Polygon,4756) NOT NULL
);
 ,   DROP TABLE public.giaothong_surface_cautau;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            A           1259    84556    giaothong_surface_nhomautau    TABLE     }  CREATE TABLE public.giaothong_surface_nhomautau (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    "GM_Surface" public.geometry(Polygon,4756) NOT NULL
);
 /   DROP TABLE public.giaothong_surface_nhomautau;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            G           1259    84634    multimedia_dulieudaphuongtien    TABLE     �  CREATE TABLE public.multimedia_dulieudaphuongtien (
    "maNhanDang" character varying(20) NOT NULL,
    "tenDuLieu" character varying(100),
    "pathDuLieu" character varying(100) NOT NULL,
    "ngayDuLieu" timestamp with time zone,
    "duLieuAnhDaiDien" boolean NOT NULL,
    "duLieuMoTa" boolean NOT NULL,
    "maNhanDangObj" character varying(30) NOT NULL,
    "lopDL_id" character varying(50) NOT NULL
);
 1   DROP TABLE public.multimedia_dulieudaphuongtien;
       public         heap    postgres    false            B           1259    84592    multimedia_loaistyle    TABLE     �   CREATE TABLE public.multimedia_loaistyle (
    "maNhanDang" character varying(20) NOT NULL,
    "tenLoaiStyle" character varying(100) NOT NULL,
    "ghiChu" character varying(500)
);
 (   DROP TABLE public.multimedia_loaistyle;
       public         heap    postgres    false            C           1259    84600    multimedia_lopdulieu    TABLE     �  CREATE TABLE public.multimedia_lopdulieu (
    "maNhanDang" character varying(50) NOT NULL,
    "tenHienThiLop" character varying(100),
    "publicGeoserver" boolean NOT NULL,
    "pathPublic" character varying(200),
    "hienThiLopChuyenDe" boolean NOT NULL,
    "thuTuHienThi" integer NOT NULL,
    "kieuLop" integer NOT NULL,
    "nhomDL_id" character varying(50) NOT NULL,
    content_type_id integer NOT NULL
);
 (   DROP TABLE public.multimedia_lopdulieu;
       public         heap    postgres    false            F           1259    84621    multimedia_metadata    TABLE     
  CREATE TABLE public.multimedia_metadata (
    "maNhanDang" character varying(20) NOT NULL,
    "tenMetaData" character varying(50) NOT NULL,
    "XMLMetaData" text,
    "PathMetaData" character varying(100) NOT NULL,
    "maLop_id" character varying(50) NOT NULL
);
 '   DROP TABLE public.multimedia_metadata;
       public         heap    postgres    false            D           1259    84605    multimedia_nhomdulieu    TABLE     �   CREATE TABLE public.multimedia_nhomdulieu (
    "maNhanDang" character varying(50) NOT NULL,
    "moTaNhom" character varying(500),
    "tenNhom" character varying(50)
);
 )   DROP TABLE public.multimedia_nhomdulieu;
       public         heap    postgres    false            E           1259    84613    multimedia_style    TABLE     �  CREATE TABLE public.multimedia_style (
    "maNhanDang" character varying(20) NOT NULL,
    "tenStyle" character varying(100) NOT NULL,
    "kieuDinhDangStyle" integer NOT NULL,
    "ngayStyle" timestamp with time zone,
    "hienThi" boolean NOT NULL,
    "styleXML" text,
    "styleCSS" text,
    "stylePath" character varying(100),
    "maLoaiStyle_id" character varying(20) NOT NULL,
    "maLop_id" character varying(50) NOT NULL
);
 $   DROP TABLE public.multimedia_style;
       public         heap    postgres    false            H           1259    84675    phubemat_bematcongtrinh    TABLE     �  CREATE TABLE public.phubemat_bematcongtrinh (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "GM_Surface" public.geometry(Polygon,4756) NOT NULL,
    "maDoiTuong" character varying(50) NOT NULL,
    "thucVat" integer NOT NULL
);
 +   DROP TABLE public.phubemat_bematcongtrinh;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            I           1259    84683    phubemat_bematkhudancu    TABLE     �  CREATE TABLE public.phubemat_bematkhudancu (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "GM_Surface" public.geometry(Polygon,4756) NOT NULL,
    "maDoiTuong" character varying(50) NOT NULL,
    "thucVat" integer NOT NULL
);
 *   DROP TABLE public.phubemat_bematkhudancu;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            J           1259    84691    phubemat_caydoclap    TABLE     �  CREATE TABLE public.phubemat_caydoclap (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    "tenCay" character varying(255) NOT NULL,
    "chieuCao" double precision NOT NULL,
    "GM_Point" public.geometry(Point,4756) NOT NULL
);
 &   DROP TABLE public.phubemat_caydoclap;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            K           1259    84699    phubemat_dattrong    TABLE     �  CREATE TABLE public.phubemat_dattrong (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "GM_Surface" public.geometry(Polygon,4756) NOT NULL,
    "maDoiTuong" character varying(50) NOT NULL,
    ten character varying(255)
);
 %   DROP TABLE public.phubemat_dattrong;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            L           1259    84707    phubemat_nuocmat    TABLE     r  CREATE TABLE public.phubemat_nuocmat (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "GM_Surface" public.geometry(Polygon,4756) NOT NULL,
    "maDoiTuong" character varying(50) NOT NULL
);
 $   DROP TABLE public.phubemat_nuocmat;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            M           1259    84715    phubemat_ranhgioiphubemat    TABLE     �  CREATE TABLE public.phubemat_ranhgioiphubemat (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    "loaiRanhGioiPhuBeMat" integer NOT NULL,
    "GM_Curve" public.geometry(LineString,4756) NOT NULL
);
 -   DROP TABLE public.phubemat_ranhgioiphubemat;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            N           1259    84723    phubemat_thucvatdaybien    TABLE     y  CREATE TABLE public.phubemat_thucvatdaybien (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "GM_Surface" public.geometry(Polygon,4756) NOT NULL,
    "maDoiTuong" character varying(50) NOT NULL
);
 +   DROP TABLE public.phubemat_thucvatdaybien;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            ]           1259    84879    soanthaokehoach_diemnvdh    TABLE       CREATE TABLE public.soanthaokehoach_diemnvdh (
    "maNhanDang" character varying(50) NOT NULL,
    "tenDiem" character varying(100) NOT NULL,
    "moTaDiem" text,
    "ngayDiem" date,
    "geoDiem" public.geometry(Point,4756) NOT NULL,
    nvdh_id character varying(50) NOT NULL
);
 ,   DROP TABLE public.soanthaokehoach_diemnvdh;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            P           1259    84755    soanthaokehoach_ganlucluong    TABLE       CREATE TABLE public.soanthaokehoach_ganlucluong (
    "maNhanDang" character varying(50) NOT NULL,
    "tenGanLL" character varying(100) NOT NULL,
    "noiDungNhiemVuGanLL" text NOT NULL,
    "quanSoGanLL" integer,
    "donViGanLL" character varying(50) NOT NULL,
    "thoiGianBDau" timestamp with time zone,
    "thoiGianKThuc" timestamp with time zone,
    "trangThaiLL" integer NOT NULL,
    pat_id character varying(50) NOT NULL,
    pav_id character varying(50) NOT NULL,
    pavt_id character varying(50) NOT NULL
);
 /   DROP TABLE public.soanthaokehoach_ganlucluong;
       public         heap    postgres    false            Q           1259    84763    soanthaokehoach_nvbp    TABLE     ]  CREATE TABLE public.soanthaokehoach_nvbp (
    "maNhanDang" character varying(50) NOT NULL,
    "tenNVBP" character varying(100) NOT NULL,
    "moTaNVBP" text NOT NULL,
    "ngayBDNVBP" date,
    "ngayKTNVBP" date,
    "trangThaiNVBP" integer NOT NULL,
    "maDV_id" character varying(20) NOT NULL,
    "maNVDH_id" character varying(50) NOT NULL
);
 (   DROP TABLE public.soanthaokehoach_nvbp;
       public         heap    postgres    false            R           1259    84771    soanthaokehoach_nvdh    TABLE        CREATE TABLE public.soanthaokehoach_nvdh (
    "maNhanDang" character varying(50) NOT NULL,
    "tenNVDH" character varying(100) NOT NULL,
    "moTaNV" text,
    "chihuyNVDH" character varying(50) NOT NULL,
    "ngayBDNVDH" date,
    "ngayKTNVDH" date,
    "kieuNVDH" integer NOT NULL
);
 (   DROP TABLE public.soanthaokehoach_nvdh;
       public         heap    postgres    false            \           1259    84851 !   soanthaokehoach_pheduyetchungnvbp    TABLE     5  CREATE TABLE public.soanthaokehoach_pheduyetchungnvbp (
    "maNhanDang" character varying(50) NOT NULL,
    "tenCMNVBP" character varying(50) NOT NULL,
    "moTaCMNVBP" text,
    "nguoiCMNVBP" text,
    "ngayCMNVBP" date,
    "trangThaiCMNVBP" integer NOT NULL,
    nvbp_id character varying(50) NOT NULL
);
 5   DROP TABLE public.soanthaokehoach_pheduyetchungnvbp;
       public         heap    postgres    false            [           1259    84843 +   soanthaokehoach_pheduyetphuonganganlucluong    TABLE     n  CREATE TABLE public.soanthaokehoach_pheduyetphuonganganlucluong (
    "maNhanDang" character varying(50) NOT NULL,
    "cmNoiDungNhiemVuGanLL" text NOT NULL,
    "cmQuanSoGanLL" integer,
    "cmDonViGanLL" text NOT NULL,
    "cmThoiGianBDau" date,
    "cmThoiGianKThuc" date,
    "trangThaiCMGanLL" integer NOT NULL,
    "ganLL_id" character varying(50) NOT NULL
);
 ?   DROP TABLE public.soanthaokehoach_pheduyetphuonganganlucluong;
       public         heap    postgres    false            Z           1259    84835 %   soanthaokehoach_pheduyetphuongantuyen    TABLE     i  CREATE TABLE public.soanthaokehoach_pheduyetphuongantuyen (
    "maNhanDang" character varying(50) NOT NULL,
    "moTaCMPATuyen" text NOT NULL,
    "nguoiCMPATuyen" character varying(50),
    "ngayCMPATuyen" date,
    "trangThaiCMPATuyen" integer NOT NULL,
    "geoCMPATuyen" public.geometry(LineString,4756),
    "paTuyen_id" character varying(50) NOT NULL
);
 9   DROP TABLE public.soanthaokehoach_pheduyetphuongantuyen;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            Y           1259    84827 %   soanthaokehoach_pheduyetphuonganvitri    TABLE     U  CREATE TABLE public.soanthaokehoach_pheduyetphuonganvitri (
    "maNhanDang" character varying(50) NOT NULL,
    "moTaCMPAVT" text NOT NULL,
    "nguoiCMPAVT" character varying(50),
    "ngayCMPAVT" date,
    "trangThaiCMPAVT" integer NOT NULL,
    "geoCMPAVT" public.geometry(Point,4756),
    "paViTri_id" character varying(50) NOT NULL
);
 9   DROP TABLE public.soanthaokehoach_pheduyetphuonganvitri;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            X           1259    84819 $   soanthaokehoach_pheduyetphuonganvung    TABLE     _  CREATE TABLE public.soanthaokehoach_pheduyetphuonganvung (
    "maNhanDang" character varying(50) NOT NULL,
    "moTaCMPAVung" text NOT NULL,
    "nguoiCMPAVung" character varying(50),
    "ngayCMPAVung" date,
    "trangThaiCMPAVung" integer NOT NULL,
    "geoCMPAVung" public.geometry(Polygon,4756),
    "paVung_id" character varying(50) NOT NULL
);
 8   DROP TABLE public.soanthaokehoach_pheduyetphuonganvung;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            W           1259    84811    soanthaokehoach_phuongantuyen    TABLE     �  CREATE TABLE public.soanthaokehoach_phuongantuyen (
    "maNhanDang" character varying(50) NOT NULL,
    "tenPATuyen" character varying(100) NOT NULL,
    "moTaPATuyen" text NOT NULL,
    "nguoiPATuyen" character varying(50),
    "ngayPATuyen" date,
    "kieuPATuyen" integer NOT NULL,
    "trangThaiPATuyen" integer NOT NULL,
    "geoPATuyen" public.geometry(LineString,4756) NOT NULL,
    nvbp_id character varying(50) NOT NULL
);
 1   DROP TABLE public.soanthaokehoach_phuongantuyen;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            V           1259    84803    soanthaokehoach_phuonganvitri    TABLE     �  CREATE TABLE public.soanthaokehoach_phuonganvitri (
    "maNhanDang" character varying(50) NOT NULL,
    "tenPAVT" character varying(100) NOT NULL,
    "moTaPAVT" text NOT NULL,
    "nguoiPAVT" character varying(50),
    "ngayPAVT" date,
    "kieuPAVT" integer NOT NULL,
    "trangthaiPAVT" integer NOT NULL,
    "geoPAVT" public.geometry(Point,4756) NOT NULL,
    nvbp_id character varying(50) NOT NULL
);
 1   DROP TABLE public.soanthaokehoach_phuonganvitri;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            U           1259    84795    soanthaokehoach_phuonganvung    TABLE     �  CREATE TABLE public.soanthaokehoach_phuonganvung (
    "maNhanDang" character varying(50) NOT NULL,
    "tenPAVung" character varying(100) NOT NULL,
    "moTaPAVung" text NOT NULL,
    "nguoiPAVung" character varying(50),
    "ngayPAVung" date,
    "kieuPAVung" integer NOT NULL,
    "trangThaiPAVung" integer NOT NULL,
    "geoPAVung" public.geometry(Polygon,4756) NOT NULL,
    nvbp_id character varying(50) NOT NULL
);
 0   DROP TABLE public.soanthaokehoach_phuonganvung;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            T           1259    84787    soanthaokehoach_tuyennvdh    TABLE     %  CREATE TABLE public.soanthaokehoach_tuyennvdh (
    "maNhanDang" character varying(50) NOT NULL,
    "tenTuyen" character varying(100) NOT NULL,
    "moTaTuyen" text,
    "ngayTuyen" date,
    "geoTuyen" public.geometry(LineString,4756) NOT NULL,
    nvdh_id character varying(50) NOT NULL
);
 -   DROP TABLE public.soanthaokehoach_tuyennvdh;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            S           1259    84779    soanthaokehoach_vungnvdh    TABLE       CREATE TABLE public.soanthaokehoach_vungnvdh (
    "maNhanDang" character varying(50) NOT NULL,
    "tenVung" character varying(100) NOT NULL,
    "moTaVung" text,
    "ngayVung" date,
    "geoVung" public.geometry(Polygon,4756) NOT NULL,
    nvdh_id character varying(50) NOT NULL
);
 ,   DROP TABLE public.soanthaokehoach_vungnvdh;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            {           1259    85635    test_mymodel    TABLE     �   CREATE TABLE public.test_mymodel (
    id character varying(20) NOT NULL,
    label character varying(50) NOT NULL,
    choice_id integer NOT NULL
);
     DROP TABLE public.test_mymodel;
       public         heap    postgres    false            z           1259    85560    test_usecontenttype    TABLE     �   CREATE TABLE public.test_usecontenttype (
    "maNhanDang_id" integer NOT NULL,
    label character varying(20) NOT NULL,
    choice character varying(50) NOT NULL
);
 '   DROP TABLE public.test_usecontenttype;
       public         heap    postgres    false            ^           1259    85002    thuyvan_bokebocap    TABLE     �  CREATE TABLE public.thuyvan_bokebocap (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    ten character varying(255),
    "loaiChatLieu" integer NOT NULL,
    "loaiThanhPhan" integer NOT NULL,
    "GM_Curve" public.geometry(LineString,4756) NOT NULL
);
 %   DROP TABLE public.thuyvan_bokebocap;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            _           1259    85010    thuyvan_curve_kenhmuong    TABLE     �  CREATE TABLE public.thuyvan_curve_kenhmuong (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    ten character varying(255),
    "loaiHienTrangSuDung" integer NOT NULL,
    "chieuRong" double precision NOT NULL,
    "GM_Curve" public.geometry(LineString,4756) NOT NULL
);
 +   DROP TABLE public.thuyvan_curve_kenhmuong;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            `           1259    85018    thuyvan_diemdocaomucnuoc    TABLE     �  CREATE TABLE public.thuyvan_diemdocaomucnuoc (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    "doCao" double precision NOT NULL,
    "GM_Point" public.geometry(Point,4756) NOT NULL
);
 ,   DROP TABLE public.thuyvan_diemdocaomucnuoc;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            a           1259    85026    thuyvan_duongbonuoc    TABLE     �  CREATE TABLE public.thuyvan_duongbonuoc (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "GM_Curve" public.geometry(LineString,4756) NOT NULL,
    "maDoiTuong" character varying(50) NOT NULL,
    "loaiTrangThaiDuongBoNuoc" integer NOT NULL,
    "loaiDuongBoNuoc" integer NOT NULL
);
 '   DROP TABLE public.thuyvan_duongbonuoc;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            b           1259    85034    thuyvan_duongmepnuoc    TABLE     �  CREATE TABLE public.thuyvan_duongmepnuoc (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "GM_Curve" public.geometry(LineString,4756) NOT NULL,
    "maDoiTuong" character varying(50) NOT NULL,
    "loaiDuongMepNuoc" integer NOT NULL
);
 (   DROP TABLE public.thuyvan_duongmepnuoc;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            c           1259    85042    thuyvan_point_baiboi    TABLE     �  CREATE TABLE public.thuyvan_point_baiboi (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    ten character varying(255),
    "loaiBaiBoi" integer NOT NULL,
    "trangThaiXuatLo" integer NOT NULL,
    "GM_Point" public.geometry(Point,4756) NOT NULL
);
 (   DROP TABLE public.thuyvan_point_baiboi;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            d           1259    85050    thuyvan_point_baidaduoinuoc    TABLE     �  CREATE TABLE public.thuyvan_point_baidaduoinuoc (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    ten character varying(255),
    "trangThaiXuatLo" integer NOT NULL,
    "GM_Point" public.geometry(Point,4756) NOT NULL
);
 /   DROP TABLE public.thuyvan_point_baidaduoinuoc;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            e           1259    85058    thuyvan_point_biendao    TABLE     �  CREATE TABLE public.thuyvan_point_biendao (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    ten character varying(255),
    "GM_Point" public.geometry(Point,4756) NOT NULL
);
 )   DROP TABLE public.thuyvan_point_biendao;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            f           1259    85066    thuyvan_point_dao    TABLE     �  CREATE TABLE public.thuyvan_point_dao (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    ten character varying(255) NOT NULL,
    "loaiTrangThaiXuatLo" integer NOT NULL,
    "GM_Point" public.geometry(Point,4756) NOT NULL
);
 %   DROP TABLE public.thuyvan_point_dao;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            g           1259    85074    thuyvan_point_nguonnuoc    TABLE     �  CREATE TABLE public.thuyvan_point_nguonnuoc (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    ten character varying(255),
    "loaiNguonNuoc" integer NOT NULL,
    "GM_Point" public.geometry(Point,4756) NOT NULL
);
 +   DROP TABLE public.thuyvan_point_nguonnuoc;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            h           1259    85082    thuyvan_ranhgioinuocmatquyuoc    TABLE     �  CREATE TABLE public.thuyvan_ranhgioinuocmatquyuoc (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "GM_Curve" public.geometry(LineString,4756) NOT NULL,
    "maDoiTuong" character varying(50) NOT NULL,
    "loaiRanhGioiNuocMatQuyUoc" integer NOT NULL
);
 1   DROP TABLE public.thuyvan_ranhgioinuocmatquyuoc;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            u           1259    85164    thuyvan_songgiodongchay    TABLE     �  CREATE TABLE public.thuyvan_songgiodongchay (
    id bigint NOT NULL,
    "maSongGioDongChay" character varying(50) NOT NULL,
    "thoigianThuThap" timestamp with time zone,
    "huongThang1" character varying(50) NOT NULL,
    "giaTriThang1" double precision NOT NULL,
    "huongThang2" character varying(50) NOT NULL,
    "giaTriThang2" double precision NOT NULL,
    "huongThang3" character varying(50) NOT NULL,
    "giaTriThang3" double precision NOT NULL,
    "huongThang4" character varying(50) NOT NULL,
    "giaTriThang4" double precision NOT NULL,
    "huongThang5" character varying(50) NOT NULL,
    "giaTriThang5" double precision NOT NULL,
    "huongThang6" character varying(50) NOT NULL,
    "giaTriThang6" double precision NOT NULL,
    "huongThang7" character varying(50) NOT NULL,
    "giaTriThang7" double precision NOT NULL,
    "huongThang8" character varying(50) NOT NULL,
    "giaTriThang8" double precision NOT NULL,
    "huongThang9" character varying(50) NOT NULL,
    "giaTriThang9" double precision NOT NULL,
    "huongThang10" character varying(50) NOT NULL,
    "giaTriThang10" double precision NOT NULL,
    "huongThang11" character varying(50) NOT NULL,
    "giaTriThang11" double precision NOT NULL,
    "huongThang12" character varying(50) NOT NULL,
    "giaTriThang12" double precision NOT NULL,
    "thamSo" integer NOT NULL,
    "tramKTTV_id" character varying(50) NOT NULL
);
 +   DROP TABLE public.thuyvan_songgiodongchay;
       public         heap    postgres    false            t           1259    85162    thuyvan_songgiodongchay_id_seq    SEQUENCE     �   CREATE SEQUENCE public.thuyvan_songgiodongchay_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 5   DROP SEQUENCE public.thuyvan_songgiodongchay_id_seq;
       public          postgres    false    373            �           0    0    thuyvan_songgiodongchay_id_seq    SEQUENCE OWNED BY     a   ALTER SEQUENCE public.thuyvan_songgiodongchay_id_seq OWNED BY public.thuyvan_songgiodongchay.id;
          public          postgres    false    372            i           1259    85090    thuyvan_surface_baiboi    TABLE     �  CREATE TABLE public.thuyvan_surface_baiboi (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    ten character varying(255),
    "loaiBaiBoi" integer NOT NULL,
    "trangThaiXuatLo" integer NOT NULL,
    "GM_Surface" public.geometry(Polygon,4756) NOT NULL
);
 *   DROP TABLE public.thuyvan_surface_baiboi;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            j           1259    85098    thuyvan_surface_baidaduoinuoc    TABLE     �  CREATE TABLE public.thuyvan_surface_baidaduoinuoc (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    ten character varying(255),
    "trangThaiXuatLo" integer NOT NULL,
    "GM_Surface" public.geometry(Polygon,4756) NOT NULL
);
 1   DROP TABLE public.thuyvan_surface_baidaduoinuoc;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            k           1259    85106    thuyvan_surface_biendao    TABLE     �  CREATE TABLE public.thuyvan_surface_biendao (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    ten character varying(255),
    "GM_Surface" public.geometry(Polygon,4756) NOT NULL
);
 +   DROP TABLE public.thuyvan_surface_biendao;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            l           1259    85114    thuyvan_surface_dao    TABLE     �  CREATE TABLE public.thuyvan_surface_dao (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    ten character varying(255) NOT NULL,
    "loaiTrangThaiXuatLo" integer NOT NULL,
    "GM_Surface" public.geometry(Polygon,4756) NOT NULL
);
 '   DROP TABLE public.thuyvan_surface_dao;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            m           1259    85122    thuyvan_surface_kenhmuong    TABLE     �  CREATE TABLE public.thuyvan_surface_kenhmuong (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    ten character varying(255),
    "loaiHienTrangSuDung" integer NOT NULL,
    "chieuRong" double precision NOT NULL,
    "GM_Surface" public.geometry(Polygon,4756) NOT NULL
);
 -   DROP TABLE public.thuyvan_surface_kenhmuong;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            n           1259    85130    thuyvan_surface_nguonnuoc    TABLE     �  CREATE TABLE public.thuyvan_surface_nguonnuoc (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    ten character varying(255),
    "loaiNguonNuoc" integer NOT NULL,
    "GM_Surface" public.geometry(Polygon,4756) NOT NULL
);
 -   DROP TABLE public.thuyvan_surface_nguonnuoc;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            s           1259    85156    thuyvan_thamsokttv    TABLE     �  CREATE TABLE public.thuyvan_thamsokttv (
    id bigint NOT NULL,
    "maThamSoKTTV" character varying(50) NOT NULL,
    "thoigianThuThap" timestamp with time zone,
    "giatriThang1" double precision,
    "giatriThang2" double precision,
    "giatriThang3" double precision,
    "giatriThang4" double precision,
    "giatriThang5" double precision,
    "giatriThang6" double precision,
    "giatriThang7" double precision,
    "giatriThang8" double precision,
    "giatriThang9" double precision,
    "giatriThang10" double precision,
    "giatriThang11" double precision,
    "giatriThang12" double precision,
    "thamSo" integer NOT NULL,
    "tramKTTV_id" character varying(50) NOT NULL
);
 &   DROP TABLE public.thuyvan_thamsokttv;
       public         heap    postgres    false            r           1259    85154    thuyvan_thamsokttv_id_seq    SEQUENCE     �   CREATE SEQUENCE public.thuyvan_thamsokttv_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 0   DROP SEQUENCE public.thuyvan_thamsokttv_id_seq;
       public          postgres    false    371            �           0    0    thuyvan_thamsokttv_id_seq    SEQUENCE OWNED BY     W   ALTER SEQUENCE public.thuyvan_thamsokttv_id_seq OWNED BY public.thuyvan_thamsokttv.id;
          public          postgres    false    370            q           1259    85148    thuyvan_thamsonuoc    TABLE     �  CREATE TABLE public.thuyvan_thamsonuoc (
    id bigint NOT NULL,
    "maThamSoNuoc" character varying(50) NOT NULL,
    "thoigianThuThap" timestamp with time zone,
    "giatriThang1" double precision,
    "giatriThang2" double precision,
    "giatriThang3" double precision,
    "giatriThang4" double precision,
    "giatriThang5" double precision,
    "giatriThang6" double precision,
    "giatriThang7" double precision,
    "giatriThang8" double precision,
    "giatriThang9" double precision,
    "giatriThang10" double precision,
    "giatriThang11" double precision,
    "giatriThang12" double precision,
    "tangDoSau" integer NOT NULL,
    "thamSo" integer NOT NULL,
    "tramKTTV_id" character varying(50) NOT NULL
);
 &   DROP TABLE public.thuyvan_thamsonuoc;
       public         heap    postgres    false            p           1259    85146    thuyvan_thamsonuoc_id_seq    SEQUENCE     �   CREATE SEQUENCE public.thuyvan_thamsonuoc_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 0   DROP SEQUENCE public.thuyvan_thamsonuoc_id_seq;
       public          postgres    false    369            �           0    0    thuyvan_thamsonuoc_id_seq    SEQUENCE OWNED BY     W   ALTER SEQUENCE public.thuyvan_thamsonuoc_id_seq OWNED BY public.thuyvan_thamsonuoc.id;
          public          postgres    false    368            o           1259    85138    thuyvan_tramthuthapkttv    TABLE     $  CREATE TABLE public.thuyvan_tramthuthapkttv (
    manhandang character varying(50) NOT NULL,
    phienban integer NOT NULL,
    ngayphienban timestamp with time zone NOT NULL,
    giatridochinhxacmatphang double precision,
    nguyennhanthaydoi character varying(250),
    "maDoiTuong" character varying(50) NOT NULL,
    "tenTram" character varying(255) NOT NULL,
    "loaiTramThuThapKTTV" integer NOT NULL,
    "kieuThuThapKTTV" integer NOT NULL,
    "Mota_TramKTTV" character varying(500),
    "GM_Point" public.geometry(Point,4756) NOT NULL
);
 +   DROP TABLE public.thuyvan_tramthuthapkttv;
       public         heap    postgres    false    2    2    2    2    2    2    2    2            �           2604    85522    auth_group id    DEFAULT     n   ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);
 <   ALTER TABLE public.auth_group ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    374    375    375            �           2604    85532    auth_group_permissions id    DEFAULT     �   ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);
 H   ALTER TABLE public.auth_group_permissions ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    376    377    377            �           2604    83379    auth_permission id    DEFAULT     x   ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);
 A   ALTER TABLE public.auth_permission ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    211    210    211            �           2604    84290    diahinh_solieuhkdc id    DEFAULT     ~   ALTER TABLE ONLY public.diahinh_solieuhkdc ALTER COLUMN id SET DEFAULT nextval('public.diahinh_solieuhkdc_id_seq'::regclass);
 D   ALTER TABLE public.diahinh_solieuhkdc ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    294    295    295            �           2604    83630    django_admin_log id    DEFAULT     z   ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);
 B   ALTER TABLE public.django_admin_log ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    227    228    228            �           2604    83369    django_content_type id    DEFAULT     �   ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);
 E   ALTER TABLE public.django_content_type ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    209    208    209            �           2604    83358    django_migrations id    DEFAULT     |   ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);
 C   ALTER TABLE public.django_migrations ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    207    206    207            �           2604    83508    dulieuquantri_nguoidung id    DEFAULT     �   ALTER TABLE ONLY public.dulieuquantri_nguoidung ALTER COLUMN id SET DEFAULT nextval('public.dulieuquantri_nguoidung_id_seq'::regclass);
 I   ALTER TABLE public.dulieuquantri_nguoidung ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    222    221    222            �           2604    83521 !   dulieuquantri_nguoidung_groups id    DEFAULT     �   ALTER TABLE ONLY public.dulieuquantri_nguoidung_groups ALTER COLUMN id SET DEFAULT nextval('public.dulieuquantri_nguoidung_groups_id_seq'::regclass);
 P   ALTER TABLE public.dulieuquantri_nguoidung_groups ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    223    224    224            �           2604    83529 +   dulieuquantri_nguoidung_user_permissions id    DEFAULT     �   ALTER TABLE ONLY public.dulieuquantri_nguoidung_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.dulieuquantri_nguoidung_user_permissions_id_seq'::regclass);
 Z   ALTER TABLE public.dulieuquantri_nguoidung_user_permissions ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    226    225    226            �           2604    83466    dulieuquantri_nhomtaikhoan id    DEFAULT     �   ALTER TABLE ONLY public.dulieuquantri_nhomtaikhoan ALTER COLUMN id SET DEFAULT nextval('public.dulieuquantri_nhomtaikhoan_id_seq'::regclass);
 L   ALTER TABLE public.dulieuquantri_nhomtaikhoan ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    219    218    219            �           2604    84338    eav_attribute id    DEFAULT     t   ALTER TABLE ONLY public.eav_attribute ALTER COLUMN id SET DEFAULT nextval('public.eav_attribute_id_seq'::regclass);
 ?   ALTER TABLE public.eav_attribute ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    297    296    297            �           2604    84349    eav_attribute_entity_ct id    DEFAULT     �   ALTER TABLE ONLY public.eav_attribute_entity_ct ALTER COLUMN id SET DEFAULT nextval('public.eav_attribute_entity_ct_id_seq'::regclass);
 I   ALTER TABLE public.eav_attribute_entity_ct ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    298    299    299            �           2604    84378    eav_enumgroup id    DEFAULT     t   ALTER TABLE ONLY public.eav_enumgroup ALTER COLUMN id SET DEFAULT nextval('public.eav_enumgroup_id_seq'::regclass);
 ?   ALTER TABLE public.eav_enumgroup ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    304    305    305            �           2604    84388    eav_enumgroup_values id    DEFAULT     �   ALTER TABLE ONLY public.eav_enumgroup_values ALTER COLUMN id SET DEFAULT nextval('public.eav_enumgroup_values_id_seq'::regclass);
 F   ALTER TABLE public.eav_enumgroup_values ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    307    306    307            �           2604    84357    eav_enumvalue id    DEFAULT     t   ALTER TABLE ONLY public.eav_enumvalue ALTER COLUMN id SET DEFAULT nextval('public.eav_enumvalue_id_seq'::regclass);
 ?   ALTER TABLE public.eav_enumvalue ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    301    300    301            �           2604    84367    eav_value id    DEFAULT     l   ALTER TABLE ONLY public.eav_value ALTER COLUMN id SET DEFAULT nextval('public.eav_value_id_seq'::regclass);
 ;   ALTER TABLE public.eav_value ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    302    303    303            �           2604    85167    thuyvan_songgiodongchay id    DEFAULT     �   ALTER TABLE ONLY public.thuyvan_songgiodongchay ALTER COLUMN id SET DEFAULT nextval('public.thuyvan_songgiodongchay_id_seq'::regclass);
 I   ALTER TABLE public.thuyvan_songgiodongchay ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    372    373    373            �           2604    85159    thuyvan_thamsokttv id    DEFAULT     ~   ALTER TABLE ONLY public.thuyvan_thamsokttv ALTER COLUMN id SET DEFAULT nextval('public.thuyvan_thamsokttv_id_seq'::regclass);
 D   ALTER TABLE public.thuyvan_thamsokttv ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    371    370    371            �           2604    85151    thuyvan_thamsonuoc id    DEFAULT     ~   ALTER TABLE ONLY public.thuyvan_thamsonuoc ALTER COLUMN id SET DEFAULT nextval('public.thuyvan_thamsonuoc_id_seq'::regclass);
 D   ALTER TABLE public.thuyvan_thamsonuoc ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    369    368    369            �          0    85519 
   auth_group 
   TABLE DATA                 public          postgres    false    375   #Y      �          0    85529    auth_group_permissions 
   TABLE DATA                 public          postgres    false    377   �Y                0    83376    auth_permission 
   TABLE DATA                 public          postgres    false    211   �Y      /          0    83651 (   biengioidiagioi_diaphanhanhchinhtrenbien 
   TABLE DATA                 public          postgres    false    229   �x      0          0    83659 +   biengioidiagioi_diaphanhanhchinhtrendatlien 
   TABLE DATA                 public          postgres    false    230   �x      1          0    83667 .   biengioidiagioi_duongranhgioihanhchinhtrenbien 
   TABLE DATA                 public          postgres    false    231   �x      2          0    83675    biengioidiagioi_vungbien 
   TABLE DATA                 public          postgres    false    232   Xz      3          0    83691    cosododac_diemdodacquocgia 
   TABLE DATA                 public          postgres    false    233   rz      4          0    83699    cosododac_diemgocdodacquocgia 
   TABLE DATA                 public          postgres    false    234   �z      5          0    83707 !   cosododac_tramdinhvivetinhquocgia 
   TABLE DATA                 public          postgres    false    235   �{      6          0    83721    dancu_congtrinhcongnghiep 
   TABLE DATA                 public          postgres    false    236   �|      7          0    83729    dancu_cotdien 
   TABLE DATA                 public          postgres    false    237   �}      ^          0    84041    dancu_curve_congtrinhcongnghiep 
   TABLE DATA                 public          postgres    false    276   �}      8          0    83737    dancu_curve_congtrinhphutro 
   TABLE DATA                 public          postgres    false    238   �~      9          0    83745    dancu_diadanhdancu 
   TABLE DATA                 public          postgres    false    239   �~      :          0    83753    dancu_duongdaytaidien 
   TABLE DATA                 public          postgres    false    240   �~      ;          0    83761    dancu_duongongdan 
   TABLE DATA                 public          postgres    false    241   �~      <          0    83769    dancu_khoinha 
   TABLE DATA                 public          postgres    false    242         =          0    83777    dancu_khuchucnangdacthu 
   TABLE DATA                 public          postgres    false    243   -      >          0    83785    dancu_khudancu 
   TABLE DATA                 public          postgres    false    244   G      ?          0    83793    dancu_point_congtrinhanninh 
   TABLE DATA                 public          postgres    false    245   a      _          0    84049    dancu_point_congtrinhcongnghiep 
   TABLE DATA                 public          postgres    false    277   {      @          0    83801    dancu_point_congtrinhgiaoduc 
   TABLE DATA                 public          postgres    false    246   �      A          0    83809    dancu_point_congtrinhquocphong 
   TABLE DATA                 public          postgres    false    247   �      B          0    83817    dancu_point_congtrinhthethao 
   TABLE DATA                 public          postgres    false    248   ��      C          0    83825 $   dancu_point_congtrinhthuongmaidichvu 
   TABLE DATA                 public          postgres    false    249   ɀ      D          0    83833 %   dancu_point_congtrinhtongiaotinnguong 
   TABLE DATA                 public          postgres    false    250   �      E          0    83841    dancu_point_congtrinhvanhoa 
   TABLE DATA                 public          postgres    false    251   ��      F          0    83849 !   dancu_point_congtrinhxulychatthai 
   TABLE DATA                 public          postgres    false    252   �      G          0    83857    dancu_point_congtrinhyte 
   TABLE DATA                 public          postgres    false    253   1�      H          0    83865 $   dancu_point_cososanxuatnonglamnghiep 
   TABLE DATA                 public          postgres    false    254   K�      I          0    83873    dancu_point_hatangkythuatkhac 
   TABLE DATA                 public          postgres    false    255   e�      J          0    83881    dancu_point_nha 
   TABLE DATA                 public          postgres    false    256   �      K          0    83889    dancu_point_trusocoquannhanuoc 
   TABLE DATA                 public          postgres    false    257   ��      L          0    83897    dancu_ranhgioi 
   TABLE DATA                 public          postgres    false    258   ��      M          0    83905    dancu_surface_congtrinhanninh 
   TABLE DATA                 public          postgres    false    259   ́      `          0    84057 !   dancu_surface_congtrinhcongnghiep 
   TABLE DATA                 public          postgres    false    278   �      N          0    83913    dancu_surface_congtrinhgiaoduc 
   TABLE DATA                 public          postgres    false    260   �      O          0    83921    dancu_surface_congtrinhphutro 
   TABLE DATA                 public          postgres    false    261   �      P          0    83929     dancu_surface_congtrinhquocphong 
   TABLE DATA                 public          postgres    false    262   5�      Q          0    83937    dancu_surface_congtrinhthethao 
   TABLE DATA                 public          postgres    false    263   O�      R          0    83945 &   dancu_surface_congtrinhthuongmaidichvu 
   TABLE DATA                 public          postgres    false    264   i�      S          0    83953 '   dancu_surface_congtrinhtongiaotinnguong 
   TABLE DATA                 public          postgres    false    265   ��      T          0    83961    dancu_surface_congtrinhvanhoa 
   TABLE DATA                 public          postgres    false    266   ��      U          0    83969 #   dancu_surface_congtrinhxulychatthai 
   TABLE DATA                 public          postgres    false    267   ��      V          0    83977    dancu_surface_congtrinhyte 
   TABLE DATA                 public          postgres    false    268   т      W          0    83985 &   dancu_surface_cososanxuatnonglamnghiep 
   TABLE DATA                 public          postgres    false    269   �      X          0    83993    dancu_surface_hatangkythuatkhac 
   TABLE DATA                 public          postgres    false    270   �      Y          0    84001    dancu_surface_nha 
   TABLE DATA                 public          postgres    false    271   �      Z          0    84009     dancu_surface_trusocoquannhanuoc 
   TABLE DATA                 public          postgres    false    272   9�      [          0    84017     dancu_tramkhituongthuyvanquocgia 
   TABLE DATA                 public          postgres    false    273   S�      \          0    84025    dancu_tramquantracmoitruong 
   TABLE DATA                 public          postgres    false    274   m�      ]          0    84033    dancu_tramquantractainguyennuoc 
   TABLE DATA                 public          postgres    false    275   ��      a          0    84165    diahinh_chatday 
   TABLE DATA                 public          postgres    false    279   ��      b          0    84173 #   diahinh_curve_diahinhdacbietdaybien 
   TABLE DATA                 public          postgres    false    280   ��      c          0    84181    diahinh_diamao 
   TABLE DATA                 public          postgres    false    281   Ճ      d          0    84189    diahinh_diemdocao 
   TABLE DATA                 public          postgres    false    282   �      e          0    84197    diahinh_diemdosau 
   TABLE DATA                 public          postgres    false    283   	�      f          0    84205    diahinh_duongbinhdo 
   TABLE DATA                 public          postgres    false    284   #�      g          0    84213    diahinh_duongbinhdosau 
   TABLE DATA                 public          postgres    false    285   =�      h          0    84221    diahinh_hokhoandiachat 
   TABLE DATA                 public          postgres    false    286   W�      i          0    84229    diahinh_loaidiachat 
   TABLE DATA                 public          postgres    false    287   q�      j          0    84237    diahinh_matcatdienhinh 
   TABLE DATA                 public          postgres    false    288   ��      k          0    84245    diahinh_mohinhsodocaogoclopdiem 
   TABLE DATA                 public          postgres    false    289   ��      l          0    84253     diahinh_mohinhsodocaogoclopduong 
   TABLE DATA                 public          postgres    false    290   ��      m          0    84261    diahinh_mohinhsodocaogoclopvung 
   TABLE DATA                 public          postgres    false    291   ل      n          0    84269 &   diahinh_mohinhsodocaogoclopvungbientap 
   TABLE DATA                 public          postgres    false    292   �      q          0    84287    diahinh_solieuhkdc 
   TABLE DATA                 public          postgres    false    295   �      o          0    84277 %   diahinh_surface_diahinhdacbietdaybien 
   TABLE DATA                 public          postgres    false    293   '�      .          0    83627    django_admin_log 
   TABLE DATA                 public          postgres    false    228   A�                0    83366    django_content_type 
   TABLE DATA                 public          postgres    false    209   �                0    83355    django_migrations 
   TABLE DATA                 public          postgres    false    207   ��      �          0    84745    django_session 
   TABLE DATA                 public          postgres    false    335   I�                0    83388    dulieuquantri_bienchetrangbi 
   TABLE DATA                 public          postgres    false    212   ��                0    83397    dulieuquantri_capdonvi 
   TABLE DATA                 public          postgres    false    213   T�      &          0    83474    dulieuquantri_donvi 
   TABLE DATA                 public          postgres    false    220   �                 0    83423    dulieuquantri_loaidonvi 
   TABLE DATA                 public          postgres    false    214   �      !          0    83431    dulieuquantri_loaitrangbikhitai 
   TABLE DATA                 public          postgres    false    215   ��      (          0    83505    dulieuquantri_nguoidung 
   TABLE DATA                 public          postgres    false    222   ��      *          0    83518    dulieuquantri_nguoidung_groups 
   TABLE DATA                 public          postgres    false    224   ��      ,          0    83526 (   dulieuquantri_nguoidung_user_permissions 
   TABLE DATA                 public          postgres    false    226   �      %          0    83463    dulieuquantri_nhomtaikhoan 
   TABLE DATA                 public          postgres    false    219   ��      �          0    91827    dulieuquantri_thietbikhitai 
   TABLE DATA                 public          postgres    false    380   1�      "          0    83439    dulieuquantri_tinhtrangtrangbi 
   TABLE DATA                 public          postgres    false    216   q�      #          0    83447    dulieuquantri_xuatxu 
   TABLE DATA                 public          postgres    false    217   �      s          0    84335    eav_attribute 
   TABLE DATA                 public          postgres    false    297   ÿ      u          0    84346    eav_attribute_entity_ct 
   TABLE DATA                 public          postgres    false    299   !�      {          0    84375    eav_enumgroup 
   TABLE DATA                 public          postgres    false    305   ��      }          0    84385    eav_enumgroup_values 
   TABLE DATA                 public          postgres    false    307   ��      w          0    84354    eav_enumvalue 
   TABLE DATA                 public          postgres    false    301   ��      y          0    84364 	   eav_value 
   TABLE DATA                 public          postgres    false    303   ��      ~          0    84452    giaothong_baidaptructhang 
   TABLE DATA                 public          postgres    false    308   �                0    84460 )   giaothong_baohieudanluonghanghaiduongthuy 
   TABLE DATA                 public          postgres    false    309   -�      �          0    84468    giaothong_baohieuhanghaiais 
   TABLE DATA                 public          postgres    false    310   G�      �          0    84476    giaothong_bencang 
   TABLE DATA                 public          postgres    false    311   a�      �          0    84484    giaothong_curve_cautau 
   TABLE DATA                 public          postgres    false    312   {�      �          0    84492    giaothong_curve_conggiaothong 
   TABLE DATA                 public          postgres    false    313   ��      �          0    84500    giaothong_curve_nhomautau 
   TABLE DATA                 public          postgres    false    314   ��      �          0    84508    giaothong_duongbang 
   TABLE DATA                 public          postgres    false    315   ��      �          0    84516    giaothong_duongbo 
   TABLE DATA                 public          postgres    false    316   ��      �          0    84524 (   giaothong_point_cacdoituonghanghaihaivan 
   TABLE DATA                 public          postgres    false    317   ��      �          0    84532    giaothong_point_conggiaothong 
   TABLE DATA                 public          postgres    false    318   �      �          0    84540 *   giaothong_surface_cacdoituonghanghaihaivan 
   TABLE DATA                 public          postgres    false    319   1�      �          0    84548    giaothong_surface_cautau 
   TABLE DATA                 public          postgres    false    320   K�      �          0    84556    giaothong_surface_nhomautau 
   TABLE DATA                 public          postgres    false    321   e�      �          0    84634    multimedia_dulieudaphuongtien 
   TABLE DATA                 public          postgres    false    327   �      �          0    84592    multimedia_loaistyle 
   TABLE DATA                 public          postgres    false    322   ��      �          0    84600    multimedia_lopdulieu 
   TABLE DATA                 public          postgres    false    323   �      �          0    84621    multimedia_metadata 
   TABLE DATA                 public          postgres    false    326   ��      �          0    84605    multimedia_nhomdulieu 
   TABLE DATA                 public          postgres    false    324   ��      �          0    84613    multimedia_style 
   TABLE DATA                 public          postgres    false    325   ~�      �          0    84675    phubemat_bematcongtrinh 
   TABLE DATA                 public          postgres    false    328   ��      �          0    84683    phubemat_bematkhudancu 
   TABLE DATA                 public          postgres    false    329   ��      �          0    84691    phubemat_caydoclap 
   TABLE DATA                 public          postgres    false    330   ��      �          0    84699    phubemat_dattrong 
   TABLE DATA                 public          postgres    false    331   ��      �          0    84707    phubemat_nuocmat 
   TABLE DATA                 public          postgres    false    332    �      �          0    84715    phubemat_ranhgioiphubemat 
   TABLE DATA                 public          postgres    false    333   �      �          0    84723    phubemat_thucvatdaybien 
   TABLE DATA                 public          postgres    false    334   4�      �          0    84879    soanthaokehoach_diemnvdh 
   TABLE DATA                 public          postgres    false    349   N�      �          0    84755    soanthaokehoach_ganlucluong 
   TABLE DATA                 public          postgres    false    336   h�      �          0    84763    soanthaokehoach_nvbp 
   TABLE DATA                 public          postgres    false    337   ��      �          0    84771    soanthaokehoach_nvdh 
   TABLE DATA                 public          postgres    false    338   ��      �          0    84851 !   soanthaokehoach_pheduyetchungnvbp 
   TABLE DATA                 public          postgres    false    348   Y�      �          0    84843 +   soanthaokehoach_pheduyetphuonganganlucluong 
   TABLE DATA                 public          postgres    false    347   s�      �          0    84835 %   soanthaokehoach_pheduyetphuongantuyen 
   TABLE DATA                 public          postgres    false    346   ��      �          0    84827 %   soanthaokehoach_pheduyetphuonganvitri 
   TABLE DATA                 public          postgres    false    345   ��      �          0    84819 $   soanthaokehoach_pheduyetphuonganvung 
   TABLE DATA                 public          postgres    false    344   ��      �          0    84811    soanthaokehoach_phuongantuyen 
   TABLE DATA                 public          postgres    false    343   ��      �          0    84803    soanthaokehoach_phuonganvitri 
   TABLE DATA                 public          postgres    false    342   ��      �          0    84795    soanthaokehoach_phuonganvung 
   TABLE DATA                 public          postgres    false    341   �      �          0    84787    soanthaokehoach_tuyennvdh 
   TABLE DATA                 public          postgres    false    340   )�      �          0    84779    soanthaokehoach_vungnvdh 
   TABLE DATA                 public          postgres    false    339   C�      �          0    82649    spatial_ref_sys 
   TABLE DATA                 public          postgres    false    202   ]�      �          0    85635    test_mymodel 
   TABLE DATA                 public          postgres    false    379   w�      �          0    85560    test_usecontenttype 
   TABLE DATA                 public          postgres    false    378   #�      �          0    85002    thuyvan_bokebocap 
   TABLE DATA                 public          postgres    false    350   ��      �          0    85010    thuyvan_curve_kenhmuong 
   TABLE DATA                 public          postgres    false    351   ��      �          0    85018    thuyvan_diemdocaomucnuoc 
   TABLE DATA                 public          postgres    false    352   �      �          0    85026    thuyvan_duongbonuoc 
   TABLE DATA                 public          postgres    false    353   /�      �          0    85034    thuyvan_duongmepnuoc 
   TABLE DATA                 public          postgres    false    354   I�      �          0    85042    thuyvan_point_baiboi 
   TABLE DATA                 public          postgres    false    355   c�      �          0    85050    thuyvan_point_baidaduoinuoc 
   TABLE DATA                 public          postgres    false    356   }�      �          0    85058    thuyvan_point_biendao 
   TABLE DATA                 public          postgres    false    357   ��      �          0    85066    thuyvan_point_dao 
   TABLE DATA                 public          postgres    false    358   ��      �          0    85074    thuyvan_point_nguonnuoc 
   TABLE DATA                 public          postgres    false    359   ��      �          0    85082    thuyvan_ranhgioinuocmatquyuoc 
   TABLE DATA                 public          postgres    false    360   ��      �          0    85164    thuyvan_songgiodongchay 
   TABLE DATA                 public          postgres    false    373   ��      �          0    85090    thuyvan_surface_baiboi 
   TABLE DATA                 public          postgres    false    361   �      �          0    85098    thuyvan_surface_baidaduoinuoc 
   TABLE DATA                 public          postgres    false    362   3�      �          0    85106    thuyvan_surface_biendao 
   TABLE DATA                 public          postgres    false    363   M�      �          0    85114    thuyvan_surface_dao 
   TABLE DATA                 public          postgres    false    364   g�      �          0    85122    thuyvan_surface_kenhmuong 
   TABLE DATA                 public          postgres    false    365   ��      �          0    85130    thuyvan_surface_nguonnuoc 
   TABLE DATA                 public          postgres    false    366   ��      �          0    85156    thuyvan_thamsokttv 
   TABLE DATA                 public          postgres    false    371   ��      �          0    85148    thuyvan_thamsonuoc 
   TABLE DATA                 public          postgres    false    369   ��      �          0    85138    thuyvan_tramthuthapkttv 
   TABLE DATA                 public          postgres    false    367   ��      �           0    0    auth_group_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.auth_group_id_seq', 23, true);
          public          postgres    false    374            �           0    0    auth_group_permissions_id_seq    SEQUENCE SET     N   SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 5448, true);
          public          postgres    false    376            �           0    0    auth_permission_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.auth_permission_id_seq', 611, true);
          public          postgres    false    210            �           0    0    diahinh_solieuhkdc_id_seq    SEQUENCE SET     H   SELECT pg_catalog.setval('public.diahinh_solieuhkdc_id_seq', 1, false);
          public          postgres    false    294            �           0    0    django_admin_log_id_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.django_admin_log_id_seq', 237, true);
          public          postgres    false    227            �           0    0    django_content_type_id_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('public.django_content_type_id_seq', 152, true);
          public          postgres    false    208            �           0    0    django_migrations_id_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.django_migrations_id_seq', 86, true);
          public          postgres    false    206            �           0    0 %   dulieuquantri_nguoidung_groups_id_seq    SEQUENCE SET     S   SELECT pg_catalog.setval('public.dulieuquantri_nguoidung_groups_id_seq', 8, true);
          public          postgres    false    223            �           0    0    dulieuquantri_nguoidung_id_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public.dulieuquantri_nguoidung_id_seq', 3, true);
          public          postgres    false    221            �           0    0 /   dulieuquantri_nguoidung_user_permissions_id_seq    SEQUENCE SET     ]   SELECT pg_catalog.setval('public.dulieuquantri_nguoidung_user_permissions_id_seq', 3, true);
          public          postgres    false    225            �           0    0 !   dulieuquantri_nhomtaikhoan_id_seq    SEQUENCE SET     P   SELECT pg_catalog.setval('public.dulieuquantri_nhomtaikhoan_id_seq', 13, true);
          public          postgres    false    218            �           0    0    eav_attribute_entity_ct_id_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public.eav_attribute_entity_ct_id_seq', 5, true);
          public          postgres    false    298            �           0    0    eav_attribute_id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.eav_attribute_id_seq', 5, true);
          public          postgres    false    296            �           0    0    eav_enumgroup_id_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public.eav_enumgroup_id_seq', 1, false);
          public          postgres    false    304            �           0    0    eav_enumgroup_values_id_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('public.eav_enumgroup_values_id_seq', 1, false);
          public          postgres    false    306            �           0    0    eav_enumvalue_id_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public.eav_enumvalue_id_seq', 1, false);
          public          postgres    false    300            �           0    0    eav_value_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.eav_value_id_seq', 4, true);
          public          postgres    false    302            �           0    0    thuyvan_songgiodongchay_id_seq    SEQUENCE SET     M   SELECT pg_catalog.setval('public.thuyvan_songgiodongchay_id_seq', 1, false);
          public          postgres    false    372            �           0    0    thuyvan_thamsokttv_id_seq    SEQUENCE SET     H   SELECT pg_catalog.setval('public.thuyvan_thamsokttv_id_seq', 1, false);
          public          postgres    false    370            �           0    0    thuyvan_thamsonuoc_id_seq    SEQUENCE SET     H   SELECT pg_catalog.setval('public.thuyvan_thamsonuoc_id_seq', 1, false);
          public          postgres    false    368            9           2606    85526    auth_group auth_group_name_key 
   CONSTRAINT     Y   ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);
 H   ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_name_key;
       public            postgres    false    375            >           2606    85537 R   auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);
 |   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq;
       public            postgres    false    377    377            A           2606    85534 2   auth_group_permissions auth_group_permissions_pkey 
   CONSTRAINT     p   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);
 \   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_pkey;
       public            postgres    false    377            ;           2606    85524    auth_group auth_group_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_pkey;
       public            postgres    false    375            �           2606    83650 F   auth_permission auth_permission_content_type_id_codename_01ab375a_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);
 p   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq;
       public            postgres    false    211    211            �           2606    83381 $   auth_permission auth_permission_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);
 N   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_pkey;
       public            postgres    false    211            �           2606    83658 V   biengioidiagioi_diaphanhanhchinhtrenbien biengioidiagioi_diaphanhanhchinhtrenbien_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.biengioidiagioi_diaphanhanhchinhtrenbien
    ADD CONSTRAINT biengioidiagioi_diaphanhanhchinhtrenbien_pkey PRIMARY KEY (manhandang);
 �   ALTER TABLE ONLY public.biengioidiagioi_diaphanhanhchinhtrenbien DROP CONSTRAINT biengioidiagioi_diaphanhanhchinhtrenbien_pkey;
       public            postgres    false    229            �           2606    83666 \   biengioidiagioi_diaphanhanhchinhtrendatlien biengioidiagioi_diaphanhanhchinhtrendatlien_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.biengioidiagioi_diaphanhanhchinhtrendatlien
    ADD CONSTRAINT biengioidiagioi_diaphanhanhchinhtrendatlien_pkey PRIMARY KEY (manhandang);
 �   ALTER TABLE ONLY public.biengioidiagioi_diaphanhanhchinhtrendatlien DROP CONSTRAINT biengioidiagioi_diaphanhanhchinhtrendatlien_pkey;
       public            postgres    false    230            �           2606    83674 b   biengioidiagioi_duongranhgioihanhchinhtrenbien biengioidiagioi_duongranhgioihanhchinhtrenbien_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.biengioidiagioi_duongranhgioihanhchinhtrenbien
    ADD CONSTRAINT biengioidiagioi_duongranhgioihanhchinhtrenbien_pkey PRIMARY KEY (manhandang);
 �   ALTER TABLE ONLY public.biengioidiagioi_duongranhgioihanhchinhtrenbien DROP CONSTRAINT biengioidiagioi_duongranhgioihanhchinhtrenbien_pkey;
       public            postgres    false    231                        2606    83682 6   biengioidiagioi_vungbien biengioidiagioi_vungbien_pkey 
   CONSTRAINT     |   ALTER TABLE ONLY public.biengioidiagioi_vungbien
    ADD CONSTRAINT biengioidiagioi_vungbien_pkey PRIMARY KEY (manhandang);
 `   ALTER TABLE ONLY public.biengioidiagioi_vungbien DROP CONSTRAINT biengioidiagioi_vungbien_pkey;
       public            postgres    false    232                       2606    83698 :   cosododac_diemdodacquocgia cosododac_diemdodacquocgia_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.cosododac_diemdodacquocgia
    ADD CONSTRAINT cosododac_diemdodacquocgia_pkey PRIMARY KEY (manhandang);
 d   ALTER TABLE ONLY public.cosododac_diemdodacquocgia DROP CONSTRAINT cosododac_diemdodacquocgia_pkey;
       public            postgres    false    233                       2606    83706 @   cosododac_diemgocdodacquocgia cosododac_diemgocdodacquocgia_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.cosododac_diemgocdodacquocgia
    ADD CONSTRAINT cosododac_diemgocdodacquocgia_pkey PRIMARY KEY (manhandang);
 j   ALTER TABLE ONLY public.cosododac_diemgocdodacquocgia DROP CONSTRAINT cosododac_diemgocdodacquocgia_pkey;
       public            postgres    false    234                       2606    83714 H   cosododac_tramdinhvivetinhquocgia cosododac_tramdinhvivetinhquocgia_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.cosododac_tramdinhvivetinhquocgia
    ADD CONSTRAINT cosododac_tramdinhvivetinhquocgia_pkey PRIMARY KEY (manhandang);
 r   ALTER TABLE ONLY public.cosododac_tramdinhvivetinhquocgia DROP CONSTRAINT cosododac_tramdinhvivetinhquocgia_pkey;
       public            postgres    false    235                       2606    83728 8   dancu_congtrinhcongnghiep dancu_congtrinhcongnghiep_pkey 
   CONSTRAINT     ~   ALTER TABLE ONLY public.dancu_congtrinhcongnghiep
    ADD CONSTRAINT dancu_congtrinhcongnghiep_pkey PRIMARY KEY (manhandang);
 b   ALTER TABLE ONLY public.dancu_congtrinhcongnghiep DROP CONSTRAINT dancu_congtrinhcongnghiep_pkey;
       public            postgres    false    236                       2606    83736     dancu_cotdien dancu_cotdien_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.dancu_cotdien
    ADD CONSTRAINT dancu_cotdien_pkey PRIMARY KEY (manhandang);
 J   ALTER TABLE ONLY public.dancu_cotdien DROP CONSTRAINT dancu_cotdien_pkey;
       public            postgres    false    237            �           2606    84048 D   dancu_curve_congtrinhcongnghiep dancu_curve_congtrinhcongnghiep_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.dancu_curve_congtrinhcongnghiep
    ADD CONSTRAINT dancu_curve_congtrinhcongnghiep_pkey PRIMARY KEY (congtrinhcongnghiep_ptr_id);
 n   ALTER TABLE ONLY public.dancu_curve_congtrinhcongnghiep DROP CONSTRAINT dancu_curve_congtrinhcongnghiep_pkey;
       public            postgres    false    276                       2606    83744 <   dancu_curve_congtrinhphutro dancu_curve_congtrinhphutro_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.dancu_curve_congtrinhphutro
    ADD CONSTRAINT dancu_curve_congtrinhphutro_pkey PRIMARY KEY (manhandang);
 f   ALTER TABLE ONLY public.dancu_curve_congtrinhphutro DROP CONSTRAINT dancu_curve_congtrinhphutro_pkey;
       public            postgres    false    238                       2606    83752 *   dancu_diadanhdancu dancu_diadanhdancu_pkey 
   CONSTRAINT     p   ALTER TABLE ONLY public.dancu_diadanhdancu
    ADD CONSTRAINT dancu_diadanhdancu_pkey PRIMARY KEY (manhandang);
 T   ALTER TABLE ONLY public.dancu_diadanhdancu DROP CONSTRAINT dancu_diadanhdancu_pkey;
       public            postgres    false    239                       2606    83760 0   dancu_duongdaytaidien dancu_duongdaytaidien_pkey 
   CONSTRAINT     v   ALTER TABLE ONLY public.dancu_duongdaytaidien
    ADD CONSTRAINT dancu_duongdaytaidien_pkey PRIMARY KEY (manhandang);
 Z   ALTER TABLE ONLY public.dancu_duongdaytaidien DROP CONSTRAINT dancu_duongdaytaidien_pkey;
       public            postgres    false    240            #           2606    83768 (   dancu_duongongdan dancu_duongongdan_pkey 
   CONSTRAINT     n   ALTER TABLE ONLY public.dancu_duongongdan
    ADD CONSTRAINT dancu_duongongdan_pkey PRIMARY KEY (manhandang);
 R   ALTER TABLE ONLY public.dancu_duongongdan DROP CONSTRAINT dancu_duongongdan_pkey;
       public            postgres    false    241            '           2606    83776     dancu_khoinha dancu_khoinha_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.dancu_khoinha
    ADD CONSTRAINT dancu_khoinha_pkey PRIMARY KEY (manhandang);
 J   ALTER TABLE ONLY public.dancu_khoinha DROP CONSTRAINT dancu_khoinha_pkey;
       public            postgres    false    242            +           2606    83784 4   dancu_khuchucnangdacthu dancu_khuchucnangdacthu_pkey 
   CONSTRAINT     z   ALTER TABLE ONLY public.dancu_khuchucnangdacthu
    ADD CONSTRAINT dancu_khuchucnangdacthu_pkey PRIMARY KEY (manhandang);
 ^   ALTER TABLE ONLY public.dancu_khuchucnangdacthu DROP CONSTRAINT dancu_khuchucnangdacthu_pkey;
       public            postgres    false    243            /           2606    83792 "   dancu_khudancu dancu_khudancu_pkey 
   CONSTRAINT     h   ALTER TABLE ONLY public.dancu_khudancu
    ADD CONSTRAINT dancu_khudancu_pkey PRIMARY KEY (manhandang);
 L   ALTER TABLE ONLY public.dancu_khudancu DROP CONSTRAINT dancu_khudancu_pkey;
       public            postgres    false    244            3           2606    83800 <   dancu_point_congtrinhanninh dancu_point_congtrinhanninh_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.dancu_point_congtrinhanninh
    ADD CONSTRAINT dancu_point_congtrinhanninh_pkey PRIMARY KEY (manhandang);
 f   ALTER TABLE ONLY public.dancu_point_congtrinhanninh DROP CONSTRAINT dancu_point_congtrinhanninh_pkey;
       public            postgres    false    245            �           2606    84056 D   dancu_point_congtrinhcongnghiep dancu_point_congtrinhcongnghiep_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.dancu_point_congtrinhcongnghiep
    ADD CONSTRAINT dancu_point_congtrinhcongnghiep_pkey PRIMARY KEY (congtrinhcongnghiep_ptr_id);
 n   ALTER TABLE ONLY public.dancu_point_congtrinhcongnghiep DROP CONSTRAINT dancu_point_congtrinhcongnghiep_pkey;
       public            postgres    false    277            7           2606    83808 >   dancu_point_congtrinhgiaoduc dancu_point_congtrinhgiaoduc_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.dancu_point_congtrinhgiaoduc
    ADD CONSTRAINT dancu_point_congtrinhgiaoduc_pkey PRIMARY KEY (manhandang);
 h   ALTER TABLE ONLY public.dancu_point_congtrinhgiaoduc DROP CONSTRAINT dancu_point_congtrinhgiaoduc_pkey;
       public            postgres    false    246            ;           2606    83816 B   dancu_point_congtrinhquocphong dancu_point_congtrinhquocphong_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.dancu_point_congtrinhquocphong
    ADD CONSTRAINT dancu_point_congtrinhquocphong_pkey PRIMARY KEY (manhandang);
 l   ALTER TABLE ONLY public.dancu_point_congtrinhquocphong DROP CONSTRAINT dancu_point_congtrinhquocphong_pkey;
       public            postgres    false    247            ?           2606    83824 >   dancu_point_congtrinhthethao dancu_point_congtrinhthethao_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.dancu_point_congtrinhthethao
    ADD CONSTRAINT dancu_point_congtrinhthethao_pkey PRIMARY KEY (manhandang);
 h   ALTER TABLE ONLY public.dancu_point_congtrinhthethao DROP CONSTRAINT dancu_point_congtrinhthethao_pkey;
       public            postgres    false    248            C           2606    83832 N   dancu_point_congtrinhthuongmaidichvu dancu_point_congtrinhthuongmaidichvu_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.dancu_point_congtrinhthuongmaidichvu
    ADD CONSTRAINT dancu_point_congtrinhthuongmaidichvu_pkey PRIMARY KEY (manhandang);
 x   ALTER TABLE ONLY public.dancu_point_congtrinhthuongmaidichvu DROP CONSTRAINT dancu_point_congtrinhthuongmaidichvu_pkey;
       public            postgres    false    249            G           2606    83840 P   dancu_point_congtrinhtongiaotinnguong dancu_point_congtrinhtongiaotinnguong_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.dancu_point_congtrinhtongiaotinnguong
    ADD CONSTRAINT dancu_point_congtrinhtongiaotinnguong_pkey PRIMARY KEY (manhandang);
 z   ALTER TABLE ONLY public.dancu_point_congtrinhtongiaotinnguong DROP CONSTRAINT dancu_point_congtrinhtongiaotinnguong_pkey;
       public            postgres    false    250            K           2606    83848 <   dancu_point_congtrinhvanhoa dancu_point_congtrinhvanhoa_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.dancu_point_congtrinhvanhoa
    ADD CONSTRAINT dancu_point_congtrinhvanhoa_pkey PRIMARY KEY (manhandang);
 f   ALTER TABLE ONLY public.dancu_point_congtrinhvanhoa DROP CONSTRAINT dancu_point_congtrinhvanhoa_pkey;
       public            postgres    false    251            O           2606    83856 H   dancu_point_congtrinhxulychatthai dancu_point_congtrinhxulychatthai_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.dancu_point_congtrinhxulychatthai
    ADD CONSTRAINT dancu_point_congtrinhxulychatthai_pkey PRIMARY KEY (manhandang);
 r   ALTER TABLE ONLY public.dancu_point_congtrinhxulychatthai DROP CONSTRAINT dancu_point_congtrinhxulychatthai_pkey;
       public            postgres    false    252            S           2606    83864 6   dancu_point_congtrinhyte dancu_point_congtrinhyte_pkey 
   CONSTRAINT     |   ALTER TABLE ONLY public.dancu_point_congtrinhyte
    ADD CONSTRAINT dancu_point_congtrinhyte_pkey PRIMARY KEY (manhandang);
 `   ALTER TABLE ONLY public.dancu_point_congtrinhyte DROP CONSTRAINT dancu_point_congtrinhyte_pkey;
       public            postgres    false    253            W           2606    83872 N   dancu_point_cososanxuatnonglamnghiep dancu_point_cososanxuatnonglamnghiep_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.dancu_point_cososanxuatnonglamnghiep
    ADD CONSTRAINT dancu_point_cososanxuatnonglamnghiep_pkey PRIMARY KEY (manhandang);
 x   ALTER TABLE ONLY public.dancu_point_cososanxuatnonglamnghiep DROP CONSTRAINT dancu_point_cososanxuatnonglamnghiep_pkey;
       public            postgres    false    254            [           2606    83880 @   dancu_point_hatangkythuatkhac dancu_point_hatangkythuatkhac_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.dancu_point_hatangkythuatkhac
    ADD CONSTRAINT dancu_point_hatangkythuatkhac_pkey PRIMARY KEY (manhandang);
 j   ALTER TABLE ONLY public.dancu_point_hatangkythuatkhac DROP CONSTRAINT dancu_point_hatangkythuatkhac_pkey;
       public            postgres    false    255            _           2606    83888 $   dancu_point_nha dancu_point_nha_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.dancu_point_nha
    ADD CONSTRAINT dancu_point_nha_pkey PRIMARY KEY (manhandang);
 N   ALTER TABLE ONLY public.dancu_point_nha DROP CONSTRAINT dancu_point_nha_pkey;
       public            postgres    false    256            c           2606    83896 B   dancu_point_trusocoquannhanuoc dancu_point_trusocoquannhanuoc_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.dancu_point_trusocoquannhanuoc
    ADD CONSTRAINT dancu_point_trusocoquannhanuoc_pkey PRIMARY KEY (manhandang);
 l   ALTER TABLE ONLY public.dancu_point_trusocoquannhanuoc DROP CONSTRAINT dancu_point_trusocoquannhanuoc_pkey;
       public            postgres    false    257            g           2606    83904 "   dancu_ranhgioi dancu_ranhgioi_pkey 
   CONSTRAINT     h   ALTER TABLE ONLY public.dancu_ranhgioi
    ADD CONSTRAINT dancu_ranhgioi_pkey PRIMARY KEY (manhandang);
 L   ALTER TABLE ONLY public.dancu_ranhgioi DROP CONSTRAINT dancu_ranhgioi_pkey;
       public            postgres    false    258            k           2606    83912 @   dancu_surface_congtrinhanninh dancu_surface_congtrinhanninh_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.dancu_surface_congtrinhanninh
    ADD CONSTRAINT dancu_surface_congtrinhanninh_pkey PRIMARY KEY (manhandang);
 j   ALTER TABLE ONLY public.dancu_surface_congtrinhanninh DROP CONSTRAINT dancu_surface_congtrinhanninh_pkey;
       public            postgres    false    259            �           2606    84064 H   dancu_surface_congtrinhcongnghiep dancu_surface_congtrinhcongnghiep_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.dancu_surface_congtrinhcongnghiep
    ADD CONSTRAINT dancu_surface_congtrinhcongnghiep_pkey PRIMARY KEY (congtrinhcongnghiep_ptr_id);
 r   ALTER TABLE ONLY public.dancu_surface_congtrinhcongnghiep DROP CONSTRAINT dancu_surface_congtrinhcongnghiep_pkey;
       public            postgres    false    278            o           2606    83920 B   dancu_surface_congtrinhgiaoduc dancu_surface_congtrinhgiaoduc_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.dancu_surface_congtrinhgiaoduc
    ADD CONSTRAINT dancu_surface_congtrinhgiaoduc_pkey PRIMARY KEY (manhandang);
 l   ALTER TABLE ONLY public.dancu_surface_congtrinhgiaoduc DROP CONSTRAINT dancu_surface_congtrinhgiaoduc_pkey;
       public            postgres    false    260            s           2606    83928 @   dancu_surface_congtrinhphutro dancu_surface_congtrinhphutro_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.dancu_surface_congtrinhphutro
    ADD CONSTRAINT dancu_surface_congtrinhphutro_pkey PRIMARY KEY (manhandang);
 j   ALTER TABLE ONLY public.dancu_surface_congtrinhphutro DROP CONSTRAINT dancu_surface_congtrinhphutro_pkey;
       public            postgres    false    261            w           2606    83936 F   dancu_surface_congtrinhquocphong dancu_surface_congtrinhquocphong_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.dancu_surface_congtrinhquocphong
    ADD CONSTRAINT dancu_surface_congtrinhquocphong_pkey PRIMARY KEY (manhandang);
 p   ALTER TABLE ONLY public.dancu_surface_congtrinhquocphong DROP CONSTRAINT dancu_surface_congtrinhquocphong_pkey;
       public            postgres    false    262            {           2606    83944 B   dancu_surface_congtrinhthethao dancu_surface_congtrinhthethao_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.dancu_surface_congtrinhthethao
    ADD CONSTRAINT dancu_surface_congtrinhthethao_pkey PRIMARY KEY (manhandang);
 l   ALTER TABLE ONLY public.dancu_surface_congtrinhthethao DROP CONSTRAINT dancu_surface_congtrinhthethao_pkey;
       public            postgres    false    263                       2606    83952 R   dancu_surface_congtrinhthuongmaidichvu dancu_surface_congtrinhthuongmaidichvu_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.dancu_surface_congtrinhthuongmaidichvu
    ADD CONSTRAINT dancu_surface_congtrinhthuongmaidichvu_pkey PRIMARY KEY (manhandang);
 |   ALTER TABLE ONLY public.dancu_surface_congtrinhthuongmaidichvu DROP CONSTRAINT dancu_surface_congtrinhthuongmaidichvu_pkey;
       public            postgres    false    264            �           2606    83960 T   dancu_surface_congtrinhtongiaotinnguong dancu_surface_congtrinhtongiaotinnguong_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.dancu_surface_congtrinhtongiaotinnguong
    ADD CONSTRAINT dancu_surface_congtrinhtongiaotinnguong_pkey PRIMARY KEY (manhandang);
 ~   ALTER TABLE ONLY public.dancu_surface_congtrinhtongiaotinnguong DROP CONSTRAINT dancu_surface_congtrinhtongiaotinnguong_pkey;
       public            postgres    false    265            �           2606    83968 @   dancu_surface_congtrinhvanhoa dancu_surface_congtrinhvanhoa_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.dancu_surface_congtrinhvanhoa
    ADD CONSTRAINT dancu_surface_congtrinhvanhoa_pkey PRIMARY KEY (manhandang);
 j   ALTER TABLE ONLY public.dancu_surface_congtrinhvanhoa DROP CONSTRAINT dancu_surface_congtrinhvanhoa_pkey;
       public            postgres    false    266            �           2606    83976 L   dancu_surface_congtrinhxulychatthai dancu_surface_congtrinhxulychatthai_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.dancu_surface_congtrinhxulychatthai
    ADD CONSTRAINT dancu_surface_congtrinhxulychatthai_pkey PRIMARY KEY (manhandang);
 v   ALTER TABLE ONLY public.dancu_surface_congtrinhxulychatthai DROP CONSTRAINT dancu_surface_congtrinhxulychatthai_pkey;
       public            postgres    false    267            �           2606    83984 :   dancu_surface_congtrinhyte dancu_surface_congtrinhyte_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.dancu_surface_congtrinhyte
    ADD CONSTRAINT dancu_surface_congtrinhyte_pkey PRIMARY KEY (manhandang);
 d   ALTER TABLE ONLY public.dancu_surface_congtrinhyte DROP CONSTRAINT dancu_surface_congtrinhyte_pkey;
       public            postgres    false    268            �           2606    83992 R   dancu_surface_cososanxuatnonglamnghiep dancu_surface_cososanxuatnonglamnghiep_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.dancu_surface_cososanxuatnonglamnghiep
    ADD CONSTRAINT dancu_surface_cososanxuatnonglamnghiep_pkey PRIMARY KEY (manhandang);
 |   ALTER TABLE ONLY public.dancu_surface_cososanxuatnonglamnghiep DROP CONSTRAINT dancu_surface_cososanxuatnonglamnghiep_pkey;
       public            postgres    false    269            �           2606    84000 D   dancu_surface_hatangkythuatkhac dancu_surface_hatangkythuatkhac_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.dancu_surface_hatangkythuatkhac
    ADD CONSTRAINT dancu_surface_hatangkythuatkhac_pkey PRIMARY KEY (manhandang);
 n   ALTER TABLE ONLY public.dancu_surface_hatangkythuatkhac DROP CONSTRAINT dancu_surface_hatangkythuatkhac_pkey;
       public            postgres    false    270            �           2606    84008 (   dancu_surface_nha dancu_surface_nha_pkey 
   CONSTRAINT     n   ALTER TABLE ONLY public.dancu_surface_nha
    ADD CONSTRAINT dancu_surface_nha_pkey PRIMARY KEY (manhandang);
 R   ALTER TABLE ONLY public.dancu_surface_nha DROP CONSTRAINT dancu_surface_nha_pkey;
       public            postgres    false    271            �           2606    84016 F   dancu_surface_trusocoquannhanuoc dancu_surface_trusocoquannhanuoc_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.dancu_surface_trusocoquannhanuoc
    ADD CONSTRAINT dancu_surface_trusocoquannhanuoc_pkey PRIMARY KEY (manhandang);
 p   ALTER TABLE ONLY public.dancu_surface_trusocoquannhanuoc DROP CONSTRAINT dancu_surface_trusocoquannhanuoc_pkey;
       public            postgres    false    272            �           2606    84024 F   dancu_tramkhituongthuyvanquocgia dancu_tramkhituongthuyvanquocgia_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.dancu_tramkhituongthuyvanquocgia
    ADD CONSTRAINT dancu_tramkhituongthuyvanquocgia_pkey PRIMARY KEY (manhandang);
 p   ALTER TABLE ONLY public.dancu_tramkhituongthuyvanquocgia DROP CONSTRAINT dancu_tramkhituongthuyvanquocgia_pkey;
       public            postgres    false    273            �           2606    84032 <   dancu_tramquantracmoitruong dancu_tramquantracmoitruong_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.dancu_tramquantracmoitruong
    ADD CONSTRAINT dancu_tramquantracmoitruong_pkey PRIMARY KEY (manhandang);
 f   ALTER TABLE ONLY public.dancu_tramquantracmoitruong DROP CONSTRAINT dancu_tramquantracmoitruong_pkey;
       public            postgres    false    274            �           2606    84040 D   dancu_tramquantractainguyennuoc dancu_tramquantractainguyennuoc_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.dancu_tramquantractainguyennuoc
    ADD CONSTRAINT dancu_tramquantractainguyennuoc_pkey PRIMARY KEY (manhandang);
 n   ALTER TABLE ONLY public.dancu_tramquantractainguyennuoc DROP CONSTRAINT dancu_tramquantractainguyennuoc_pkey;
       public            postgres    false    275            �           2606    84172 $   diahinh_chatday diahinh_chatday_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.diahinh_chatday
    ADD CONSTRAINT diahinh_chatday_pkey PRIMARY KEY (manhandang);
 N   ALTER TABLE ONLY public.diahinh_chatday DROP CONSTRAINT diahinh_chatday_pkey;
       public            postgres    false    279            �           2606    84180 L   diahinh_curve_diahinhdacbietdaybien diahinh_curve_diahinhdacbietdaybien_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.diahinh_curve_diahinhdacbietdaybien
    ADD CONSTRAINT diahinh_curve_diahinhdacbietdaybien_pkey PRIMARY KEY (manhandang);
 v   ALTER TABLE ONLY public.diahinh_curve_diahinhdacbietdaybien DROP CONSTRAINT diahinh_curve_diahinhdacbietdaybien_pkey;
       public            postgres    false    280            �           2606    84188 "   diahinh_diamao diahinh_diamao_pkey 
   CONSTRAINT     h   ALTER TABLE ONLY public.diahinh_diamao
    ADD CONSTRAINT diahinh_diamao_pkey PRIMARY KEY (manhandang);
 L   ALTER TABLE ONLY public.diahinh_diamao DROP CONSTRAINT diahinh_diamao_pkey;
       public            postgres    false    281            �           2606    84196 (   diahinh_diemdocao diahinh_diemdocao_pkey 
   CONSTRAINT     n   ALTER TABLE ONLY public.diahinh_diemdocao
    ADD CONSTRAINT diahinh_diemdocao_pkey PRIMARY KEY (manhandang);
 R   ALTER TABLE ONLY public.diahinh_diemdocao DROP CONSTRAINT diahinh_diemdocao_pkey;
       public            postgres    false    282            �           2606    84204 (   diahinh_diemdosau diahinh_diemdosau_pkey 
   CONSTRAINT     n   ALTER TABLE ONLY public.diahinh_diemdosau
    ADD CONSTRAINT diahinh_diemdosau_pkey PRIMARY KEY (manhandang);
 R   ALTER TABLE ONLY public.diahinh_diemdosau DROP CONSTRAINT diahinh_diemdosau_pkey;
       public            postgres    false    283            �           2606    84212 ,   diahinh_duongbinhdo diahinh_duongbinhdo_pkey 
   CONSTRAINT     r   ALTER TABLE ONLY public.diahinh_duongbinhdo
    ADD CONSTRAINT diahinh_duongbinhdo_pkey PRIMARY KEY (manhandang);
 V   ALTER TABLE ONLY public.diahinh_duongbinhdo DROP CONSTRAINT diahinh_duongbinhdo_pkey;
       public            postgres    false    284            �           2606    84220 2   diahinh_duongbinhdosau diahinh_duongbinhdosau_pkey 
   CONSTRAINT     x   ALTER TABLE ONLY public.diahinh_duongbinhdosau
    ADD CONSTRAINT diahinh_duongbinhdosau_pkey PRIMARY KEY (manhandang);
 \   ALTER TABLE ONLY public.diahinh_duongbinhdosau DROP CONSTRAINT diahinh_duongbinhdosau_pkey;
       public            postgres    false    285            �           2606    84228 2   diahinh_hokhoandiachat diahinh_hokhoandiachat_pkey 
   CONSTRAINT     x   ALTER TABLE ONLY public.diahinh_hokhoandiachat
    ADD CONSTRAINT diahinh_hokhoandiachat_pkey PRIMARY KEY (manhandang);
 \   ALTER TABLE ONLY public.diahinh_hokhoandiachat DROP CONSTRAINT diahinh_hokhoandiachat_pkey;
       public            postgres    false    286            �           2606    84236 ,   diahinh_loaidiachat diahinh_loaidiachat_pkey 
   CONSTRAINT     r   ALTER TABLE ONLY public.diahinh_loaidiachat
    ADD CONSTRAINT diahinh_loaidiachat_pkey PRIMARY KEY (manhandang);
 V   ALTER TABLE ONLY public.diahinh_loaidiachat DROP CONSTRAINT diahinh_loaidiachat_pkey;
       public            postgres    false    287            �           2606    84244 2   diahinh_matcatdienhinh diahinh_matcatdienhinh_pkey 
   CONSTRAINT     x   ALTER TABLE ONLY public.diahinh_matcatdienhinh
    ADD CONSTRAINT diahinh_matcatdienhinh_pkey PRIMARY KEY (manhandang);
 \   ALTER TABLE ONLY public.diahinh_matcatdienhinh DROP CONSTRAINT diahinh_matcatdienhinh_pkey;
       public            postgres    false    288            �           2606    84252 D   diahinh_mohinhsodocaogoclopdiem diahinh_mohinhsodocaogoclopdiem_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.diahinh_mohinhsodocaogoclopdiem
    ADD CONSTRAINT diahinh_mohinhsodocaogoclopdiem_pkey PRIMARY KEY (manhandang);
 n   ALTER TABLE ONLY public.diahinh_mohinhsodocaogoclopdiem DROP CONSTRAINT diahinh_mohinhsodocaogoclopdiem_pkey;
       public            postgres    false    289            �           2606    84260 F   diahinh_mohinhsodocaogoclopduong diahinh_mohinhsodocaogoclopduong_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.diahinh_mohinhsodocaogoclopduong
    ADD CONSTRAINT diahinh_mohinhsodocaogoclopduong_pkey PRIMARY KEY (manhandang);
 p   ALTER TABLE ONLY public.diahinh_mohinhsodocaogoclopduong DROP CONSTRAINT diahinh_mohinhsodocaogoclopduong_pkey;
       public            postgres    false    290            �           2606    84268 D   diahinh_mohinhsodocaogoclopvung diahinh_mohinhsodocaogoclopvung_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.diahinh_mohinhsodocaogoclopvung
    ADD CONSTRAINT diahinh_mohinhsodocaogoclopvung_pkey PRIMARY KEY (manhandang);
 n   ALTER TABLE ONLY public.diahinh_mohinhsodocaogoclopvung DROP CONSTRAINT diahinh_mohinhsodocaogoclopvung_pkey;
       public            postgres    false    291            �           2606    84276 R   diahinh_mohinhsodocaogoclopvungbientap diahinh_mohinhsodocaogoclopvungbientap_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.diahinh_mohinhsodocaogoclopvungbientap
    ADD CONSTRAINT diahinh_mohinhsodocaogoclopvungbientap_pkey PRIMARY KEY (manhandang);
 |   ALTER TABLE ONLY public.diahinh_mohinhsodocaogoclopvungbientap DROP CONSTRAINT diahinh_mohinhsodocaogoclopvungbientap_pkey;
       public            postgres    false    292            �           2606    84295 *   diahinh_solieuhkdc diahinh_solieuhkdc_pkey 
   CONSTRAINT     h   ALTER TABLE ONLY public.diahinh_solieuhkdc
    ADD CONSTRAINT diahinh_solieuhkdc_pkey PRIMARY KEY (id);
 T   ALTER TABLE ONLY public.diahinh_solieuhkdc DROP CONSTRAINT diahinh_solieuhkdc_pkey;
       public            postgres    false    295            �           2606    84284 P   diahinh_surface_diahinhdacbietdaybien diahinh_surface_diahinhdacbietdaybien_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.diahinh_surface_diahinhdacbietdaybien
    ADD CONSTRAINT diahinh_surface_diahinhdacbietdaybien_pkey PRIMARY KEY (manhandang);
 z   ALTER TABLE ONLY public.diahinh_surface_diahinhdacbietdaybien DROP CONSTRAINT diahinh_surface_diahinhdacbietdaybien_pkey;
       public            postgres    false    293            �           2606    83636 &   django_admin_log django_admin_log_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_pkey;
       public            postgres    false    228            �           2606    83373 E   django_content_type django_content_type_app_label_model_76bd3d3b_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);
 o   ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq;
       public            postgres    false    209    209            �           2606    83371 ,   django_content_type django_content_type_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);
 V   ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_pkey;
       public            postgres    false    209            �           2606    83363 (   django_migrations django_migrations_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);
 R   ALTER TABLE ONLY public.django_migrations DROP CONSTRAINT django_migrations_pkey;
       public            postgres    false    207            �           2606    84752 "   django_session django_session_pkey 
   CONSTRAINT     i   ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);
 L   ALTER TABLE ONLY public.django_session DROP CONSTRAINT django_session_pkey;
       public            postgres    false    335            �           2606    83396 >   dulieuquantri_bienchetrangbi dulieuquantri_bienchetrangbi_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.dulieuquantri_bienchetrangbi
    ADD CONSTRAINT dulieuquantri_bienchetrangbi_pkey PRIMARY KEY ("maNhanDang");
 h   ALTER TABLE ONLY public.dulieuquantri_bienchetrangbi DROP CONSTRAINT dulieuquantri_bienchetrangbi_pkey;
       public            postgres    false    212            �           2606    83404 2   dulieuquantri_capdonvi dulieuquantri_capdonvi_pkey 
   CONSTRAINT     z   ALTER TABLE ONLY public.dulieuquantri_capdonvi
    ADD CONSTRAINT dulieuquantri_capdonvi_pkey PRIMARY KEY ("maNhanDang");
 \   ALTER TABLE ONLY public.dulieuquantri_capdonvi DROP CONSTRAINT dulieuquantri_capdonvi_pkey;
       public            postgres    false    213            �           2606    83482 ,   dulieuquantri_donvi dulieuquantri_donvi_pkey 
   CONSTRAINT     t   ALTER TABLE ONLY public.dulieuquantri_donvi
    ADD CONSTRAINT dulieuquantri_donvi_pkey PRIMARY KEY ("maNhanDang");
 V   ALTER TABLE ONLY public.dulieuquantri_donvi DROP CONSTRAINT dulieuquantri_donvi_pkey;
       public            postgres    false    220            �           2606    83430 4   dulieuquantri_loaidonvi dulieuquantri_loaidonvi_pkey 
   CONSTRAINT     |   ALTER TABLE ONLY public.dulieuquantri_loaidonvi
    ADD CONSTRAINT dulieuquantri_loaidonvi_pkey PRIMARY KEY ("maNhanDang");
 ^   ALTER TABLE ONLY public.dulieuquantri_loaidonvi DROP CONSTRAINT dulieuquantri_loaidonvi_pkey;
       public            postgres    false    214            �           2606    83438 >   dulieuquantri_loaitrangbikhitai dulieuquantri_loaitrangbi_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.dulieuquantri_loaitrangbikhitai
    ADD CONSTRAINT dulieuquantri_loaitrangbi_pkey PRIMARY KEY ("maNhanDang");
 h   ALTER TABLE ONLY public.dulieuquantri_loaitrangbikhitai DROP CONSTRAINT dulieuquantri_loaitrangbi_pkey;
       public            postgres    false    215            �           2606    83598 [   dulieuquantri_nguoidung_groups dulieuquantri_nguoidung__nguoidung_id_group_id_bd214449_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.dulieuquantri_nguoidung_groups
    ADD CONSTRAINT dulieuquantri_nguoidung__nguoidung_id_group_id_bd214449_uniq UNIQUE (nguoidung_id, group_id);
 �   ALTER TABLE ONLY public.dulieuquantri_nguoidung_groups DROP CONSTRAINT dulieuquantri_nguoidung__nguoidung_id_group_id_bd214449_uniq;
       public            postgres    false    224    224            �           2606    83612 h   dulieuquantri_nguoidung_user_permissions dulieuquantri_nguoidung__nguoidung_id_permission__76de0609_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.dulieuquantri_nguoidung_user_permissions
    ADD CONSTRAINT dulieuquantri_nguoidung__nguoidung_id_permission__76de0609_uniq UNIQUE (nguoidung_id, permission_id);
 �   ALTER TABLE ONLY public.dulieuquantri_nguoidung_user_permissions DROP CONSTRAINT dulieuquantri_nguoidung__nguoidung_id_permission__76de0609_uniq;
       public            postgres    false    226    226            �           2606    83523 B   dulieuquantri_nguoidung_groups dulieuquantri_nguoidung_groups_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.dulieuquantri_nguoidung_groups
    ADD CONSTRAINT dulieuquantri_nguoidung_groups_pkey PRIMARY KEY (id);
 l   ALTER TABLE ONLY public.dulieuquantri_nguoidung_groups DROP CONSTRAINT dulieuquantri_nguoidung_groups_pkey;
       public            postgres    false    224            �           2606    83513 4   dulieuquantri_nguoidung dulieuquantri_nguoidung_pkey 
   CONSTRAINT     r   ALTER TABLE ONLY public.dulieuquantri_nguoidung
    ADD CONSTRAINT dulieuquantri_nguoidung_pkey PRIMARY KEY (id);
 ^   ALTER TABLE ONLY public.dulieuquantri_nguoidung DROP CONSTRAINT dulieuquantri_nguoidung_pkey;
       public            postgres    false    222            �           2606    83531 V   dulieuquantri_nguoidung_user_permissions dulieuquantri_nguoidung_user_permissions_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.dulieuquantri_nguoidung_user_permissions
    ADD CONSTRAINT dulieuquantri_nguoidung_user_permissions_pkey PRIMARY KEY (id);
 �   ALTER TABLE ONLY public.dulieuquantri_nguoidung_user_permissions DROP CONSTRAINT dulieuquantri_nguoidung_user_permissions_pkey;
       public            postgres    false    226            �           2606    83515 <   dulieuquantri_nguoidung dulieuquantri_nguoidung_username_key 
   CONSTRAINT     {   ALTER TABLE ONLY public.dulieuquantri_nguoidung
    ADD CONSTRAINT dulieuquantri_nguoidung_username_key UNIQUE (username);
 f   ALTER TABLE ONLY public.dulieuquantri_nguoidung DROP CONSTRAINT dulieuquantri_nguoidung_username_key;
       public            postgres    false    222            �           2606    83473 B   dulieuquantri_nhomtaikhoan dulieuquantri_nhomtaikhoan_group_id_key 
   CONSTRAINT     �   ALTER TABLE ONLY public.dulieuquantri_nhomtaikhoan
    ADD CONSTRAINT dulieuquantri_nhomtaikhoan_group_id_key UNIQUE (group_id);
 l   ALTER TABLE ONLY public.dulieuquantri_nhomtaikhoan DROP CONSTRAINT dulieuquantri_nhomtaikhoan_group_id_key;
       public            postgres    false    219            �           2606    83471 :   dulieuquantri_nhomtaikhoan dulieuquantri_nhomtaikhoan_pkey 
   CONSTRAINT     x   ALTER TABLE ONLY public.dulieuquantri_nhomtaikhoan
    ADD CONSTRAINT dulieuquantri_nhomtaikhoan_pkey PRIMARY KEY (id);
 d   ALTER TABLE ONLY public.dulieuquantri_nhomtaikhoan DROP CONSTRAINT dulieuquantri_nhomtaikhoan_pkey;
       public            postgres    false    219            N           2606    91832 <   dulieuquantri_thietbikhitai dulieuquantri_thietbikhitai_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.dulieuquantri_thietbikhitai
    ADD CONSTRAINT dulieuquantri_thietbikhitai_pkey PRIMARY KEY ("maNhanDang");
 f   ALTER TABLE ONLY public.dulieuquantri_thietbikhitai DROP CONSTRAINT dulieuquantri_thietbikhitai_pkey;
       public            postgres    false    380            �           2606    83446 B   dulieuquantri_tinhtrangtrangbi dulieuquantri_tinhtrangtrangbi_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.dulieuquantri_tinhtrangtrangbi
    ADD CONSTRAINT dulieuquantri_tinhtrangtrangbi_pkey PRIMARY KEY ("maNhanDang");
 l   ALTER TABLE ONLY public.dulieuquantri_tinhtrangtrangbi DROP CONSTRAINT dulieuquantri_tinhtrangtrangbi_pkey;
       public            postgres    false    216            �           2606    83454 .   dulieuquantri_xuatxu dulieuquantri_xuatxu_pkey 
   CONSTRAINT     v   ALTER TABLE ONLY public.dulieuquantri_xuatxu
    ADD CONSTRAINT dulieuquantri_xuatxu_pkey PRIMARY KEY ("maNhanDang");
 X   ALTER TABLE ONLY public.dulieuquantri_xuatxu DROP CONSTRAINT dulieuquantri_xuatxu_pkey;
       public            postgres    false    217                        2606    84398 V   eav_attribute_entity_ct eav_attribute_entity_ct_attribute_id_contenttype_8d784edd_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.eav_attribute_entity_ct
    ADD CONSTRAINT eav_attribute_entity_ct_attribute_id_contenttype_8d784edd_uniq UNIQUE (attribute_id, contenttype_id);
 �   ALTER TABLE ONLY public.eav_attribute_entity_ct DROP CONSTRAINT eav_attribute_entity_ct_attribute_id_contenttype_8d784edd_uniq;
       public            postgres    false    299    299                       2606    84351 4   eav_attribute_entity_ct eav_attribute_entity_ct_pkey 
   CONSTRAINT     r   ALTER TABLE ONLY public.eav_attribute_entity_ct
    ADD CONSTRAINT eav_attribute_entity_ct_pkey PRIMARY KEY (id);
 ^   ALTER TABLE ONLY public.eav_attribute_entity_ct DROP CONSTRAINT eav_attribute_entity_ct_pkey;
       public            postgres    false    299            �           2606    84341     eav_attribute eav_attribute_pkey 
   CONSTRAINT     ^   ALTER TABLE ONLY public.eav_attribute
    ADD CONSTRAINT eav_attribute_pkey PRIMARY KEY (id);
 J   ALTER TABLE ONLY public.eav_attribute DROP CONSTRAINT eav_attribute_pkey;
       public            postgres    false    297            �           2606    84343 $   eav_attribute eav_attribute_slug_key 
   CONSTRAINT     _   ALTER TABLE ONLY public.eav_attribute
    ADD CONSTRAINT eav_attribute_slug_key UNIQUE (slug);
 N   ALTER TABLE ONLY public.eav_attribute DROP CONSTRAINT eav_attribute_slug_key;
       public            postgres    false    297                       2606    84382 $   eav_enumgroup eav_enumgroup_name_key 
   CONSTRAINT     _   ALTER TABLE ONLY public.eav_enumgroup
    ADD CONSTRAINT eav_enumgroup_name_key UNIQUE (name);
 N   ALTER TABLE ONLY public.eav_enumgroup DROP CONSTRAINT eav_enumgroup_name_key;
       public            postgres    false    305                       2606    84380     eav_enumgroup eav_enumgroup_pkey 
   CONSTRAINT     ^   ALTER TABLE ONLY public.eav_enumgroup
    ADD CONSTRAINT eav_enumgroup_pkey PRIMARY KEY (id);
 J   ALTER TABLE ONLY public.eav_enumgroup DROP CONSTRAINT eav_enumgroup_pkey;
       public            postgres    false    305                       2606    84438 Q   eav_enumgroup_values eav_enumgroup_values_enumgroup_id_enumvalue_id_bec52735_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.eav_enumgroup_values
    ADD CONSTRAINT eav_enumgroup_values_enumgroup_id_enumvalue_id_bec52735_uniq UNIQUE (enumgroup_id, enumvalue_id);
 {   ALTER TABLE ONLY public.eav_enumgroup_values DROP CONSTRAINT eav_enumgroup_values_enumgroup_id_enumvalue_id_bec52735_uniq;
       public            postgres    false    307    307                       2606    84390 .   eav_enumgroup_values eav_enumgroup_values_pkey 
   CONSTRAINT     l   ALTER TABLE ONLY public.eav_enumgroup_values
    ADD CONSTRAINT eav_enumgroup_values_pkey PRIMARY KEY (id);
 X   ALTER TABLE ONLY public.eav_enumgroup_values DROP CONSTRAINT eav_enumgroup_values_pkey;
       public            postgres    false    307                       2606    84359     eav_enumvalue eav_enumvalue_pkey 
   CONSTRAINT     ^   ALTER TABLE ONLY public.eav_enumvalue
    ADD CONSTRAINT eav_enumvalue_pkey PRIMARY KEY (id);
 J   ALTER TABLE ONLY public.eav_enumvalue DROP CONSTRAINT eav_enumvalue_pkey;
       public            postgres    false    301                       2606    84361 %   eav_enumvalue eav_enumvalue_value_key 
   CONSTRAINT     a   ALTER TABLE ONLY public.eav_enumvalue
    ADD CONSTRAINT eav_enumvalue_value_key UNIQUE (value);
 O   ALTER TABLE ONLY public.eav_enumvalue DROP CONSTRAINT eav_enumvalue_value_key;
       public            postgres    false    301                       2606    84372    eav_value eav_value_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.eav_value
    ADD CONSTRAINT eav_value_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.eav_value DROP CONSTRAINT eav_value_pkey;
       public            postgres    false    303                       2606    84459 8   giaothong_baidaptructhang giaothong_baidaptructhang_pkey 
   CONSTRAINT     ~   ALTER TABLE ONLY public.giaothong_baidaptructhang
    ADD CONSTRAINT giaothong_baidaptructhang_pkey PRIMARY KEY (manhandang);
 b   ALTER TABLE ONLY public.giaothong_baidaptructhang DROP CONSTRAINT giaothong_baidaptructhang_pkey;
       public            postgres    false    308            !           2606    84467 X   giaothong_baohieudanluonghanghaiduongthuy giaothong_baohieudanluonghanghaiduongthuy_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.giaothong_baohieudanluonghanghaiduongthuy
    ADD CONSTRAINT giaothong_baohieudanluonghanghaiduongthuy_pkey PRIMARY KEY (manhandang);
 �   ALTER TABLE ONLY public.giaothong_baohieudanluonghanghaiduongthuy DROP CONSTRAINT giaothong_baohieudanluonghanghaiduongthuy_pkey;
       public            postgres    false    309            %           2606    84475 <   giaothong_baohieuhanghaiais giaothong_baohieuhanghaiais_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.giaothong_baohieuhanghaiais
    ADD CONSTRAINT giaothong_baohieuhanghaiais_pkey PRIMARY KEY (manhandang);
 f   ALTER TABLE ONLY public.giaothong_baohieuhanghaiais DROP CONSTRAINT giaothong_baohieuhanghaiais_pkey;
       public            postgres    false    310            )           2606    84483 (   giaothong_bencang giaothong_bencang_pkey 
   CONSTRAINT     n   ALTER TABLE ONLY public.giaothong_bencang
    ADD CONSTRAINT giaothong_bencang_pkey PRIMARY KEY (manhandang);
 R   ALTER TABLE ONLY public.giaothong_bencang DROP CONSTRAINT giaothong_bencang_pkey;
       public            postgres    false    311            -           2606    84491 2   giaothong_curve_cautau giaothong_curve_cautau_pkey 
   CONSTRAINT     x   ALTER TABLE ONLY public.giaothong_curve_cautau
    ADD CONSTRAINT giaothong_curve_cautau_pkey PRIMARY KEY (manhandang);
 \   ALTER TABLE ONLY public.giaothong_curve_cautau DROP CONSTRAINT giaothong_curve_cautau_pkey;
       public            postgres    false    312            1           2606    84499 @   giaothong_curve_conggiaothong giaothong_curve_conggiaothong_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.giaothong_curve_conggiaothong
    ADD CONSTRAINT giaothong_curve_conggiaothong_pkey PRIMARY KEY (manhandang);
 j   ALTER TABLE ONLY public.giaothong_curve_conggiaothong DROP CONSTRAINT giaothong_curve_conggiaothong_pkey;
       public            postgres    false    313            5           2606    84507 8   giaothong_curve_nhomautau giaothong_curve_nhomautau_pkey 
   CONSTRAINT     ~   ALTER TABLE ONLY public.giaothong_curve_nhomautau
    ADD CONSTRAINT giaothong_curve_nhomautau_pkey PRIMARY KEY (manhandang);
 b   ALTER TABLE ONLY public.giaothong_curve_nhomautau DROP CONSTRAINT giaothong_curve_nhomautau_pkey;
       public            postgres    false    314            9           2606    84515 ,   giaothong_duongbang giaothong_duongbang_pkey 
   CONSTRAINT     r   ALTER TABLE ONLY public.giaothong_duongbang
    ADD CONSTRAINT giaothong_duongbang_pkey PRIMARY KEY (manhandang);
 V   ALTER TABLE ONLY public.giaothong_duongbang DROP CONSTRAINT giaothong_duongbang_pkey;
       public            postgres    false    315            =           2606    84523 (   giaothong_duongbo giaothong_duongbo_pkey 
   CONSTRAINT     n   ALTER TABLE ONLY public.giaothong_duongbo
    ADD CONSTRAINT giaothong_duongbo_pkey PRIMARY KEY (manhandang);
 R   ALTER TABLE ONLY public.giaothong_duongbo DROP CONSTRAINT giaothong_duongbo_pkey;
       public            postgres    false    316            A           2606    84531 V   giaothong_point_cacdoituonghanghaihaivan giaothong_point_cacdoituonghanghaihaivan_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.giaothong_point_cacdoituonghanghaihaivan
    ADD CONSTRAINT giaothong_point_cacdoituonghanghaihaivan_pkey PRIMARY KEY (manhandang);
 �   ALTER TABLE ONLY public.giaothong_point_cacdoituonghanghaihaivan DROP CONSTRAINT giaothong_point_cacdoituonghanghaihaivan_pkey;
       public            postgres    false    317            E           2606    84539 @   giaothong_point_conggiaothong giaothong_point_conggiaothong_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.giaothong_point_conggiaothong
    ADD CONSTRAINT giaothong_point_conggiaothong_pkey PRIMARY KEY (manhandang);
 j   ALTER TABLE ONLY public.giaothong_point_conggiaothong DROP CONSTRAINT giaothong_point_conggiaothong_pkey;
       public            postgres    false    318            I           2606    84547 Z   giaothong_surface_cacdoituonghanghaihaivan giaothong_surface_cacdoituonghanghaihaivan_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.giaothong_surface_cacdoituonghanghaihaivan
    ADD CONSTRAINT giaothong_surface_cacdoituonghanghaihaivan_pkey PRIMARY KEY (manhandang);
 �   ALTER TABLE ONLY public.giaothong_surface_cacdoituonghanghaihaivan DROP CONSTRAINT giaothong_surface_cacdoituonghanghaihaivan_pkey;
       public            postgres    false    319            M           2606    84555 6   giaothong_surface_cautau giaothong_surface_cautau_pkey 
   CONSTRAINT     |   ALTER TABLE ONLY public.giaothong_surface_cautau
    ADD CONSTRAINT giaothong_surface_cautau_pkey PRIMARY KEY (manhandang);
 `   ALTER TABLE ONLY public.giaothong_surface_cautau DROP CONSTRAINT giaothong_surface_cautau_pkey;
       public            postgres    false    320            Q           2606    84563 <   giaothong_surface_nhomautau giaothong_surface_nhomautau_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.giaothong_surface_nhomautau
    ADD CONSTRAINT giaothong_surface_nhomautau_pkey PRIMARY KEY (manhandang);
 f   ALTER TABLE ONLY public.giaothong_surface_nhomautau DROP CONSTRAINT giaothong_surface_nhomautau_pkey;
       public            postgres    false    321            o           2606    84638 @   multimedia_dulieudaphuongtien multimedia_dulieudaphuongtien_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.multimedia_dulieudaphuongtien
    ADD CONSTRAINT multimedia_dulieudaphuongtien_pkey PRIMARY KEY ("maNhanDang");
 j   ALTER TABLE ONLY public.multimedia_dulieudaphuongtien DROP CONSTRAINT multimedia_dulieudaphuongtien_pkey;
       public            postgres    false    327            T           2606    84599 .   multimedia_loaistyle multimedia_loaistyle_pkey 
   CONSTRAINT     v   ALTER TABLE ONLY public.multimedia_loaistyle
    ADD CONSTRAINT multimedia_loaistyle_pkey PRIMARY KEY ("maNhanDang");
 X   ALTER TABLE ONLY public.multimedia_loaistyle DROP CONSTRAINT multimedia_loaistyle_pkey;
       public            postgres    false    322            V           2606    85572 =   multimedia_lopdulieu multimedia_lopdulieu_content_type_id_key 
   CONSTRAINT     �   ALTER TABLE ONLY public.multimedia_lopdulieu
    ADD CONSTRAINT multimedia_lopdulieu_content_type_id_key UNIQUE (content_type_id);
 g   ALTER TABLE ONLY public.multimedia_lopdulieu DROP CONSTRAINT multimedia_lopdulieu_content_type_id_key;
       public            postgres    false    323            [           2606    85590 .   multimedia_lopdulieu multimedia_lopdulieu_pkey 
   CONSTRAINT     v   ALTER TABLE ONLY public.multimedia_lopdulieu
    ADD CONSTRAINT multimedia_lopdulieu_pkey PRIMARY KEY ("maNhanDang");
 X   ALTER TABLE ONLY public.multimedia_lopdulieu DROP CONSTRAINT multimedia_lopdulieu_pkey;
       public            postgres    false    323            j           2606    84628 ,   multimedia_metadata multimedia_metadata_pkey 
   CONSTRAINT     t   ALTER TABLE ONLY public.multimedia_metadata
    ADD CONSTRAINT multimedia_metadata_pkey PRIMARY KEY ("maNhanDang");
 V   ALTER TABLE ONLY public.multimedia_metadata DROP CONSTRAINT multimedia_metadata_pkey;
       public            postgres    false    326            ^           2606    85579 0   multimedia_nhomdulieu multimedia_nhomdulieu_pkey 
   CONSTRAINT     x   ALTER TABLE ONLY public.multimedia_nhomdulieu
    ADD CONSTRAINT multimedia_nhomdulieu_pkey PRIMARY KEY ("maNhanDang");
 Z   ALTER TABLE ONLY public.multimedia_nhomdulieu DROP CONSTRAINT multimedia_nhomdulieu_pkey;
       public            postgres    false    324            e           2606    84620 &   multimedia_style multimedia_style_pkey 
   CONSTRAINT     n   ALTER TABLE ONLY public.multimedia_style
    ADD CONSTRAINT multimedia_style_pkey PRIMARY KEY ("maNhanDang");
 P   ALTER TABLE ONLY public.multimedia_style DROP CONSTRAINT multimedia_style_pkey;
       public            postgres    false    325            s           2606    84682 4   phubemat_bematcongtrinh phubemat_bematcongtrinh_pkey 
   CONSTRAINT     z   ALTER TABLE ONLY public.phubemat_bematcongtrinh
    ADD CONSTRAINT phubemat_bematcongtrinh_pkey PRIMARY KEY (manhandang);
 ^   ALTER TABLE ONLY public.phubemat_bematcongtrinh DROP CONSTRAINT phubemat_bematcongtrinh_pkey;
       public            postgres    false    328            w           2606    84690 2   phubemat_bematkhudancu phubemat_bematkhudancu_pkey 
   CONSTRAINT     x   ALTER TABLE ONLY public.phubemat_bematkhudancu
    ADD CONSTRAINT phubemat_bematkhudancu_pkey PRIMARY KEY (manhandang);
 \   ALTER TABLE ONLY public.phubemat_bematkhudancu DROP CONSTRAINT phubemat_bematkhudancu_pkey;
       public            postgres    false    329            {           2606    84698 *   phubemat_caydoclap phubemat_caydoclap_pkey 
   CONSTRAINT     p   ALTER TABLE ONLY public.phubemat_caydoclap
    ADD CONSTRAINT phubemat_caydoclap_pkey PRIMARY KEY (manhandang);
 T   ALTER TABLE ONLY public.phubemat_caydoclap DROP CONSTRAINT phubemat_caydoclap_pkey;
       public            postgres    false    330                       2606    84706 (   phubemat_dattrong phubemat_dattrong_pkey 
   CONSTRAINT     n   ALTER TABLE ONLY public.phubemat_dattrong
    ADD CONSTRAINT phubemat_dattrong_pkey PRIMARY KEY (manhandang);
 R   ALTER TABLE ONLY public.phubemat_dattrong DROP CONSTRAINT phubemat_dattrong_pkey;
       public            postgres    false    331            �           2606    84714 &   phubemat_nuocmat phubemat_nuocmat_pkey 
   CONSTRAINT     l   ALTER TABLE ONLY public.phubemat_nuocmat
    ADD CONSTRAINT phubemat_nuocmat_pkey PRIMARY KEY (manhandang);
 P   ALTER TABLE ONLY public.phubemat_nuocmat DROP CONSTRAINT phubemat_nuocmat_pkey;
       public            postgres    false    332            �           2606    84722 8   phubemat_ranhgioiphubemat phubemat_ranhgioiphubemat_pkey 
   CONSTRAINT     ~   ALTER TABLE ONLY public.phubemat_ranhgioiphubemat
    ADD CONSTRAINT phubemat_ranhgioiphubemat_pkey PRIMARY KEY (manhandang);
 b   ALTER TABLE ONLY public.phubemat_ranhgioiphubemat DROP CONSTRAINT phubemat_ranhgioiphubemat_pkey;
       public            postgres    false    333            �           2606    84730 4   phubemat_thucvatdaybien phubemat_thucvatdaybien_pkey 
   CONSTRAINT     z   ALTER TABLE ONLY public.phubemat_thucvatdaybien
    ADD CONSTRAINT phubemat_thucvatdaybien_pkey PRIMARY KEY (manhandang);
 ^   ALTER TABLE ONLY public.phubemat_thucvatdaybien DROP CONSTRAINT phubemat_thucvatdaybien_pkey;
       public            postgres    false    334            �           2606    84886 6   soanthaokehoach_diemnvdh soanthaokehoach_diemnvdh_pkey 
   CONSTRAINT     ~   ALTER TABLE ONLY public.soanthaokehoach_diemnvdh
    ADD CONSTRAINT soanthaokehoach_diemnvdh_pkey PRIMARY KEY ("maNhanDang");
 `   ALTER TABLE ONLY public.soanthaokehoach_diemnvdh DROP CONSTRAINT soanthaokehoach_diemnvdh_pkey;
       public            postgres    false    349            �           2606    84762 <   soanthaokehoach_ganlucluong soanthaokehoach_ganlucluong_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.soanthaokehoach_ganlucluong
    ADD CONSTRAINT soanthaokehoach_ganlucluong_pkey PRIMARY KEY ("maNhanDang");
 f   ALTER TABLE ONLY public.soanthaokehoach_ganlucluong DROP CONSTRAINT soanthaokehoach_ganlucluong_pkey;
       public            postgres    false    336            �           2606    84770 .   soanthaokehoach_nvbp soanthaokehoach_nvbp_pkey 
   CONSTRAINT     v   ALTER TABLE ONLY public.soanthaokehoach_nvbp
    ADD CONSTRAINT soanthaokehoach_nvbp_pkey PRIMARY KEY ("maNhanDang");
 X   ALTER TABLE ONLY public.soanthaokehoach_nvbp DROP CONSTRAINT soanthaokehoach_nvbp_pkey;
       public            postgres    false    337            �           2606    84778 .   soanthaokehoach_nvdh soanthaokehoach_nvdh_pkey 
   CONSTRAINT     v   ALTER TABLE ONLY public.soanthaokehoach_nvdh
    ADD CONSTRAINT soanthaokehoach_nvdh_pkey PRIMARY KEY ("maNhanDang");
 X   ALTER TABLE ONLY public.soanthaokehoach_nvdh DROP CONSTRAINT soanthaokehoach_nvdh_pkey;
       public            postgres    false    338            �           2606    84858 H   soanthaokehoach_pheduyetchungnvbp soanthaokehoach_pheduyetchungnvbp_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.soanthaokehoach_pheduyetchungnvbp
    ADD CONSTRAINT soanthaokehoach_pheduyetchungnvbp_pkey PRIMARY KEY ("maNhanDang");
 r   ALTER TABLE ONLY public.soanthaokehoach_pheduyetchungnvbp DROP CONSTRAINT soanthaokehoach_pheduyetchungnvbp_pkey;
       public            postgres    false    348            �           2606    84850 \   soanthaokehoach_pheduyetphuonganganlucluong soanthaokehoach_pheduyetphuonganganlucluong_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.soanthaokehoach_pheduyetphuonganganlucluong
    ADD CONSTRAINT soanthaokehoach_pheduyetphuonganganlucluong_pkey PRIMARY KEY ("maNhanDang");
 �   ALTER TABLE ONLY public.soanthaokehoach_pheduyetphuonganganlucluong DROP CONSTRAINT soanthaokehoach_pheduyetphuonganganlucluong_pkey;
       public            postgres    false    347            �           2606    84842 P   soanthaokehoach_pheduyetphuongantuyen soanthaokehoach_pheduyetphuongantuyen_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.soanthaokehoach_pheduyetphuongantuyen
    ADD CONSTRAINT soanthaokehoach_pheduyetphuongantuyen_pkey PRIMARY KEY ("maNhanDang");
 z   ALTER TABLE ONLY public.soanthaokehoach_pheduyetphuongantuyen DROP CONSTRAINT soanthaokehoach_pheduyetphuongantuyen_pkey;
       public            postgres    false    346            �           2606    84834 P   soanthaokehoach_pheduyetphuonganvitri soanthaokehoach_pheduyetphuonganvitri_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.soanthaokehoach_pheduyetphuonganvitri
    ADD CONSTRAINT soanthaokehoach_pheduyetphuonganvitri_pkey PRIMARY KEY ("maNhanDang");
 z   ALTER TABLE ONLY public.soanthaokehoach_pheduyetphuonganvitri DROP CONSTRAINT soanthaokehoach_pheduyetphuonganvitri_pkey;
       public            postgres    false    345            �           2606    84826 N   soanthaokehoach_pheduyetphuonganvung soanthaokehoach_pheduyetphuonganvung_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.soanthaokehoach_pheduyetphuonganvung
    ADD CONSTRAINT soanthaokehoach_pheduyetphuonganvung_pkey PRIMARY KEY ("maNhanDang");
 x   ALTER TABLE ONLY public.soanthaokehoach_pheduyetphuonganvung DROP CONSTRAINT soanthaokehoach_pheduyetphuonganvung_pkey;
       public            postgres    false    344            �           2606    84818 @   soanthaokehoach_phuongantuyen soanthaokehoach_phuongantuyen_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.soanthaokehoach_phuongantuyen
    ADD CONSTRAINT soanthaokehoach_phuongantuyen_pkey PRIMARY KEY ("maNhanDang");
 j   ALTER TABLE ONLY public.soanthaokehoach_phuongantuyen DROP CONSTRAINT soanthaokehoach_phuongantuyen_pkey;
       public            postgres    false    343            �           2606    84810 @   soanthaokehoach_phuonganvitri soanthaokehoach_phuonganvitri_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.soanthaokehoach_phuonganvitri
    ADD CONSTRAINT soanthaokehoach_phuonganvitri_pkey PRIMARY KEY ("maNhanDang");
 j   ALTER TABLE ONLY public.soanthaokehoach_phuonganvitri DROP CONSTRAINT soanthaokehoach_phuonganvitri_pkey;
       public            postgres    false    342            �           2606    84802 >   soanthaokehoach_phuonganvung soanthaokehoach_phuonganvung_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.soanthaokehoach_phuonganvung
    ADD CONSTRAINT soanthaokehoach_phuonganvung_pkey PRIMARY KEY ("maNhanDang");
 h   ALTER TABLE ONLY public.soanthaokehoach_phuonganvung DROP CONSTRAINT soanthaokehoach_phuonganvung_pkey;
       public            postgres    false    341            �           2606    84794 8   soanthaokehoach_tuyennvdh soanthaokehoach_tuyennvdh_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.soanthaokehoach_tuyennvdh
    ADD CONSTRAINT soanthaokehoach_tuyennvdh_pkey PRIMARY KEY ("maNhanDang");
 b   ALTER TABLE ONLY public.soanthaokehoach_tuyennvdh DROP CONSTRAINT soanthaokehoach_tuyennvdh_pkey;
       public            postgres    false    340            �           2606    84786 6   soanthaokehoach_vungnvdh soanthaokehoach_vungnvdh_pkey 
   CONSTRAINT     ~   ALTER TABLE ONLY public.soanthaokehoach_vungnvdh
    ADD CONSTRAINT soanthaokehoach_vungnvdh_pkey PRIMARY KEY ("maNhanDang");
 `   ALTER TABLE ONLY public.soanthaokehoach_vungnvdh DROP CONSTRAINT soanthaokehoach_vungnvdh_pkey;
       public            postgres    false    339            G           2606    85639    test_mymodel test_mymodel_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.test_mymodel
    ADD CONSTRAINT test_mymodel_pkey PRIMARY KEY (id);
 H   ALTER TABLE ONLY public.test_mymodel DROP CONSTRAINT test_mymodel_pkey;
       public            postgres    false    379            C           2606    85564 ,   test_usecontenttype test_usecontenttype_pkey 
   CONSTRAINT     w   ALTER TABLE ONLY public.test_usecontenttype
    ADD CONSTRAINT test_usecontenttype_pkey PRIMARY KEY ("maNhanDang_id");
 V   ALTER TABLE ONLY public.test_usecontenttype DROP CONSTRAINT test_usecontenttype_pkey;
       public            postgres    false    378            �           2606    85009 (   thuyvan_bokebocap thuyvan_bokebocap_pkey 
   CONSTRAINT     n   ALTER TABLE ONLY public.thuyvan_bokebocap
    ADD CONSTRAINT thuyvan_bokebocap_pkey PRIMARY KEY (manhandang);
 R   ALTER TABLE ONLY public.thuyvan_bokebocap DROP CONSTRAINT thuyvan_bokebocap_pkey;
       public            postgres    false    350            �           2606    85017 4   thuyvan_curve_kenhmuong thuyvan_curve_kenhmuong_pkey 
   CONSTRAINT     z   ALTER TABLE ONLY public.thuyvan_curve_kenhmuong
    ADD CONSTRAINT thuyvan_curve_kenhmuong_pkey PRIMARY KEY (manhandang);
 ^   ALTER TABLE ONLY public.thuyvan_curve_kenhmuong DROP CONSTRAINT thuyvan_curve_kenhmuong_pkey;
       public            postgres    false    351            �           2606    85025 6   thuyvan_diemdocaomucnuoc thuyvan_diemdocaomucnuoc_pkey 
   CONSTRAINT     |   ALTER TABLE ONLY public.thuyvan_diemdocaomucnuoc
    ADD CONSTRAINT thuyvan_diemdocaomucnuoc_pkey PRIMARY KEY (manhandang);
 `   ALTER TABLE ONLY public.thuyvan_diemdocaomucnuoc DROP CONSTRAINT thuyvan_diemdocaomucnuoc_pkey;
       public            postgres    false    352            �           2606    85033 ,   thuyvan_duongbonuoc thuyvan_duongbonuoc_pkey 
   CONSTRAINT     r   ALTER TABLE ONLY public.thuyvan_duongbonuoc
    ADD CONSTRAINT thuyvan_duongbonuoc_pkey PRIMARY KEY (manhandang);
 V   ALTER TABLE ONLY public.thuyvan_duongbonuoc DROP CONSTRAINT thuyvan_duongbonuoc_pkey;
       public            postgres    false    353            �           2606    85041 .   thuyvan_duongmepnuoc thuyvan_duongmepnuoc_pkey 
   CONSTRAINT     t   ALTER TABLE ONLY public.thuyvan_duongmepnuoc
    ADD CONSTRAINT thuyvan_duongmepnuoc_pkey PRIMARY KEY (manhandang);
 X   ALTER TABLE ONLY public.thuyvan_duongmepnuoc DROP CONSTRAINT thuyvan_duongmepnuoc_pkey;
       public            postgres    false    354            �           2606    85049 .   thuyvan_point_baiboi thuyvan_point_baiboi_pkey 
   CONSTRAINT     t   ALTER TABLE ONLY public.thuyvan_point_baiboi
    ADD CONSTRAINT thuyvan_point_baiboi_pkey PRIMARY KEY (manhandang);
 X   ALTER TABLE ONLY public.thuyvan_point_baiboi DROP CONSTRAINT thuyvan_point_baiboi_pkey;
       public            postgres    false    355            �           2606    85057 <   thuyvan_point_baidaduoinuoc thuyvan_point_baidaduoinuoc_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.thuyvan_point_baidaduoinuoc
    ADD CONSTRAINT thuyvan_point_baidaduoinuoc_pkey PRIMARY KEY (manhandang);
 f   ALTER TABLE ONLY public.thuyvan_point_baidaduoinuoc DROP CONSTRAINT thuyvan_point_baidaduoinuoc_pkey;
       public            postgres    false    356                       2606    85065 0   thuyvan_point_biendao thuyvan_point_biendao_pkey 
   CONSTRAINT     v   ALTER TABLE ONLY public.thuyvan_point_biendao
    ADD CONSTRAINT thuyvan_point_biendao_pkey PRIMARY KEY (manhandang);
 Z   ALTER TABLE ONLY public.thuyvan_point_biendao DROP CONSTRAINT thuyvan_point_biendao_pkey;
       public            postgres    false    357                       2606    85073 (   thuyvan_point_dao thuyvan_point_dao_pkey 
   CONSTRAINT     n   ALTER TABLE ONLY public.thuyvan_point_dao
    ADD CONSTRAINT thuyvan_point_dao_pkey PRIMARY KEY (manhandang);
 R   ALTER TABLE ONLY public.thuyvan_point_dao DROP CONSTRAINT thuyvan_point_dao_pkey;
       public            postgres    false    358            
           2606    85081 4   thuyvan_point_nguonnuoc thuyvan_point_nguonnuoc_pkey 
   CONSTRAINT     z   ALTER TABLE ONLY public.thuyvan_point_nguonnuoc
    ADD CONSTRAINT thuyvan_point_nguonnuoc_pkey PRIMARY KEY (manhandang);
 ^   ALTER TABLE ONLY public.thuyvan_point_nguonnuoc DROP CONSTRAINT thuyvan_point_nguonnuoc_pkey;
       public            postgres    false    359                       2606    85089 @   thuyvan_ranhgioinuocmatquyuoc thuyvan_ranhgioinuocmatquyuoc_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.thuyvan_ranhgioinuocmatquyuoc
    ADD CONSTRAINT thuyvan_ranhgioinuocmatquyuoc_pkey PRIMARY KEY (manhandang);
 j   ALTER TABLE ONLY public.thuyvan_ranhgioinuocmatquyuoc DROP CONSTRAINT thuyvan_ranhgioinuocmatquyuoc_pkey;
       public            postgres    false    360            4           2606    85172 4   thuyvan_songgiodongchay thuyvan_songgiodongchay_pkey 
   CONSTRAINT     r   ALTER TABLE ONLY public.thuyvan_songgiodongchay
    ADD CONSTRAINT thuyvan_songgiodongchay_pkey PRIMARY KEY (id);
 ^   ALTER TABLE ONLY public.thuyvan_songgiodongchay DROP CONSTRAINT thuyvan_songgiodongchay_pkey;
       public            postgres    false    373                       2606    85097 2   thuyvan_surface_baiboi thuyvan_surface_baiboi_pkey 
   CONSTRAINT     x   ALTER TABLE ONLY public.thuyvan_surface_baiboi
    ADD CONSTRAINT thuyvan_surface_baiboi_pkey PRIMARY KEY (manhandang);
 \   ALTER TABLE ONLY public.thuyvan_surface_baiboi DROP CONSTRAINT thuyvan_surface_baiboi_pkey;
       public            postgres    false    361                       2606    85105 @   thuyvan_surface_baidaduoinuoc thuyvan_surface_baidaduoinuoc_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.thuyvan_surface_baidaduoinuoc
    ADD CONSTRAINT thuyvan_surface_baidaduoinuoc_pkey PRIMARY KEY (manhandang);
 j   ALTER TABLE ONLY public.thuyvan_surface_baidaduoinuoc DROP CONSTRAINT thuyvan_surface_baidaduoinuoc_pkey;
       public            postgres    false    362                       2606    85113 4   thuyvan_surface_biendao thuyvan_surface_biendao_pkey 
   CONSTRAINT     z   ALTER TABLE ONLY public.thuyvan_surface_biendao
    ADD CONSTRAINT thuyvan_surface_biendao_pkey PRIMARY KEY (manhandang);
 ^   ALTER TABLE ONLY public.thuyvan_surface_biendao DROP CONSTRAINT thuyvan_surface_biendao_pkey;
       public            postgres    false    363                       2606    85121 ,   thuyvan_surface_dao thuyvan_surface_dao_pkey 
   CONSTRAINT     r   ALTER TABLE ONLY public.thuyvan_surface_dao
    ADD CONSTRAINT thuyvan_surface_dao_pkey PRIMARY KEY (manhandang);
 V   ALTER TABLE ONLY public.thuyvan_surface_dao DROP CONSTRAINT thuyvan_surface_dao_pkey;
       public            postgres    false    364            "           2606    85129 8   thuyvan_surface_kenhmuong thuyvan_surface_kenhmuong_pkey 
   CONSTRAINT     ~   ALTER TABLE ONLY public.thuyvan_surface_kenhmuong
    ADD CONSTRAINT thuyvan_surface_kenhmuong_pkey PRIMARY KEY (manhandang);
 b   ALTER TABLE ONLY public.thuyvan_surface_kenhmuong DROP CONSTRAINT thuyvan_surface_kenhmuong_pkey;
       public            postgres    false    365            &           2606    85137 8   thuyvan_surface_nguonnuoc thuyvan_surface_nguonnuoc_pkey 
   CONSTRAINT     ~   ALTER TABLE ONLY public.thuyvan_surface_nguonnuoc
    ADD CONSTRAINT thuyvan_surface_nguonnuoc_pkey PRIMARY KEY (manhandang);
 b   ALTER TABLE ONLY public.thuyvan_surface_nguonnuoc DROP CONSTRAINT thuyvan_surface_nguonnuoc_pkey;
       public            postgres    false    366            0           2606    85161 *   thuyvan_thamsokttv thuyvan_thamsokttv_pkey 
   CONSTRAINT     h   ALTER TABLE ONLY public.thuyvan_thamsokttv
    ADD CONSTRAINT thuyvan_thamsokttv_pkey PRIMARY KEY (id);
 T   ALTER TABLE ONLY public.thuyvan_thamsokttv DROP CONSTRAINT thuyvan_thamsokttv_pkey;
       public            postgres    false    371            ,           2606    85153 *   thuyvan_thamsonuoc thuyvan_thamsonuoc_pkey 
   CONSTRAINT     h   ALTER TABLE ONLY public.thuyvan_thamsonuoc
    ADD CONSTRAINT thuyvan_thamsonuoc_pkey PRIMARY KEY (id);
 T   ALTER TABLE ONLY public.thuyvan_thamsonuoc DROP CONSTRAINT thuyvan_thamsonuoc_pkey;
       public            postgres    false    369            *           2606    85145 4   thuyvan_tramthuthapkttv thuyvan_tramthuthapkttv_pkey 
   CONSTRAINT     z   ALTER TABLE ONLY public.thuyvan_tramthuthapkttv
    ADD CONSTRAINT thuyvan_tramthuthapkttv_pkey PRIMARY KEY (manhandang);
 ^   ALTER TABLE ONLY public.thuyvan_tramthuthapkttv DROP CONSTRAINT thuyvan_tramthuthapkttv_pkey;
       public            postgres    false    367            7           1259    85535    auth_group_name_a6ea08ec_like    INDEX     h   CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);
 1   DROP INDEX public.auth_group_name_a6ea08ec_like;
       public            postgres    false    375            <           1259    85548 (   auth_group_permissions_group_id_b120cbf9    INDEX     o   CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);
 <   DROP INDEX public.auth_group_permissions_group_id_b120cbf9;
       public            postgres    false    377            ?           1259    85549 -   auth_group_permissions_permission_id_84c5c92e    INDEX     y   CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);
 A   DROP INDEX public.auth_group_permissions_permission_id_84c5c92e;
       public            postgres    false    377            �           1259    83387 (   auth_permission_content_type_id_2f476e4b    INDEX     o   CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);
 <   DROP INDEX public.auth_permission_content_type_id_2f476e4b;
       public            postgres    false    211            �           1259    83685 1   biengioidiagioi_diaphanh_maNhanDang_aa7243da_like    INDEX     �   CREATE INDEX "biengioidiagioi_diaphanh_maNhanDang_aa7243da_like" ON public.biengioidiagioi_diaphanhanhchinhtrendatlien USING btree (manhandang varchar_pattern_ops);
 G   DROP INDEX public."biengioidiagioi_diaphanh_maNhanDang_aa7243da_like";
       public            postgres    false    230            �           1259    83683 1   biengioidiagioi_diaphanh_maNhanDang_ebf18c32_like    INDEX     �   CREATE INDEX "biengioidiagioi_diaphanh_maNhanDang_ebf18c32_like" ON public.biengioidiagioi_diaphanhanhchinhtrenbien USING btree (manhandang varchar_pattern_ops);
 G   DROP INDEX public."biengioidiagioi_diaphanh_maNhanDang_ebf18c32_like";
       public            postgres    false    229            �           1259    83684 6   biengioidiagioi_diaphanhanhchinhtrenbien_GM_Surface_id    INDEX     �   CREATE INDEX "biengioidiagioi_diaphanhanhchinhtrenbien_GM_Surface_id" ON public.biengioidiagioi_diaphanhanhchinhtrenbien USING gist (gm_surface);
 L   DROP INDEX public."biengioidiagioi_diaphanhanhchinhtrenbien_GM_Surface_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    229            �           1259    83686 9   biengioidiagioi_diaphanhanhchinhtrendatlien_GM_Surface_id    INDEX     �   CREATE INDEX "biengioidiagioi_diaphanhanhchinhtrendatlien_GM_Surface_id" ON public.biengioidiagioi_diaphanhanhchinhtrendatlien USING gist ("GM_Surface");
 O   DROP INDEX public."biengioidiagioi_diaphanhanhchinhtrendatlien_GM_Surface_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    230            �           1259    83687 1   biengioidiagioi_duongran_maNhanDang_67dedb06_like    INDEX     �   CREATE INDEX "biengioidiagioi_duongran_maNhanDang_67dedb06_like" ON public.biengioidiagioi_duongranhgioihanhchinhtrenbien USING btree (manhandang varchar_pattern_ops);
 G   DROP INDEX public."biengioidiagioi_duongran_maNhanDang_67dedb06_like";
       public            postgres    false    231            �           1259    83688 :   biengioidiagioi_duongranhgioihanhchinhtrenbien_GM_Curve_id    INDEX     �   CREATE INDEX "biengioidiagioi_duongranhgioihanhchinhtrenbien_GM_Curve_id" ON public.biengioidiagioi_duongranhgioihanhchinhtrenbien USING gist ("GM_Curve");
 P   DROP INDEX public."biengioidiagioi_duongranhgioihanhchinhtrenbien_GM_Curve_id";
       public            postgres    false    231    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2            �           1259    83690 &   biengioidiagioi_vungbien_GM_Surface_id    INDEX     t   CREATE INDEX "biengioidiagioi_vungbien_GM_Surface_id" ON public.biengioidiagioi_vungbien USING gist ("GM_Surface");
 <   DROP INDEX public."biengioidiagioi_vungbien_GM_Surface_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    232            �           1259    83689 1   biengioidiagioi_vungbien_maNhanDang_df616217_like    INDEX     �   CREATE INDEX "biengioidiagioi_vungbien_maNhanDang_df616217_like" ON public.biengioidiagioi_vungbien USING btree (manhandang varchar_pattern_ops);
 G   DROP INDEX public."biengioidiagioi_vungbien_maNhanDang_df616217_like";
       public            postgres    false    232                       1259    83716 &   cosododac_diemdodacquocgia_GM_Point_id    INDEX     t   CREATE INDEX "cosododac_diemdodacquocgia_GM_Point_id" ON public.cosododac_diemdodacquocgia USING gist ("GM_Point");
 <   DROP INDEX public."cosododac_diemdodacquocgia_GM_Point_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    233                       1259    83715 3   cosododac_diemdodacquocgia_maNhanDang_a5db917b_like    INDEX     �   CREATE INDEX "cosododac_diemdodacquocgia_maNhanDang_a5db917b_like" ON public.cosododac_diemdodacquocgia USING btree (manhandang varchar_pattern_ops);
 I   DROP INDEX public."cosododac_diemdodacquocgia_maNhanDang_a5db917b_like";
       public            postgres    false    233                       1259    83718 )   cosododac_diemgocdodacquocgia_GM_Point_id    INDEX     z   CREATE INDEX "cosododac_diemgocdodacquocgia_GM_Point_id" ON public.cosododac_diemgocdodacquocgia USING gist ("GM_Point");
 ?   DROP INDEX public."cosododac_diemgocdodacquocgia_GM_Point_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    234                       1259    83717 6   cosododac_diemgocdodacquocgia_maNhanDang_f9c0db7e_like    INDEX     �   CREATE INDEX "cosododac_diemgocdodacquocgia_maNhanDang_f9c0db7e_like" ON public.cosododac_diemgocdodacquocgia USING btree (manhandang varchar_pattern_ops);
 L   DROP INDEX public."cosododac_diemgocdodacquocgia_maNhanDang_f9c0db7e_like";
       public            postgres    false    234            	           1259    83720 -   cosododac_tramdinhvivetinhquocgia_GM_Point_id    INDEX     �   CREATE INDEX "cosododac_tramdinhvivetinhquocgia_GM_Point_id" ON public.cosododac_tramdinhvivetinhquocgia USING gist ("GM_Point");
 C   DROP INDEX public."cosododac_tramdinhvivetinhquocgia_GM_Point_id";
       public            postgres    false    235    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2            
           1259    83719 :   cosododac_tramdinhvivetinhquocgia_maNhanDang_7ab4215e_like    INDEX     �   CREATE INDEX "cosododac_tramdinhvivetinhquocgia_maNhanDang_7ab4215e_like" ON public.cosododac_tramdinhvivetinhquocgia USING btree (manhandang varchar_pattern_ops);
 P   DROP INDEX public."cosododac_tramdinhvivetinhquocgia_maNhanDang_7ab4215e_like";
       public            postgres    false    235                       1259    84065 2   dancu_congtrinhcongnghiep_maNhanDang_1f264438_like    INDEX     �   CREATE INDEX "dancu_congtrinhcongnghiep_maNhanDang_1f264438_like" ON public.dancu_congtrinhcongnghiep USING btree (manhandang varchar_pattern_ops);
 H   DROP INDEX public."dancu_congtrinhcongnghiep_maNhanDang_1f264438_like";
       public            postgres    false    236                       1259    84067    dancu_cotdien_GM_Point_id    INDEX     Z   CREATE INDEX "dancu_cotdien_GM_Point_id" ON public.dancu_cotdien USING gist ("GM_Point");
 /   DROP INDEX public."dancu_cotdien_GM_Point_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    237                       1259    84066 &   dancu_cotdien_maNhanDang_c34db9b4_like    INDEX     |   CREATE INDEX "dancu_cotdien_maNhanDang_c34db9b4_like" ON public.dancu_cotdien USING btree (manhandang varchar_pattern_ops);
 <   DROP INDEX public."dancu_cotdien_maNhanDang_c34db9b4_like";
       public            postgres    false    237            �           1259    84149 ?   dancu_curve_congtrinhcon_congtrinhcongnghiep_ptr__11feb931_like    INDEX     �   CREATE INDEX dancu_curve_congtrinhcon_congtrinhcongnghiep_ptr__11feb931_like ON public.dancu_curve_congtrinhcongnghiep USING btree (congtrinhcongnghiep_ptr_id varchar_pattern_ops);
 S   DROP INDEX public.dancu_curve_congtrinhcon_congtrinhcongnghiep_ptr__11feb931_like;
       public            postgres    false    276            �           1259    84150 +   dancu_curve_congtrinhcongnghiep_GM_Curve_id    INDEX     ~   CREATE INDEX "dancu_curve_congtrinhcongnghiep_GM_Curve_id" ON public.dancu_curve_congtrinhcongnghiep USING gist ("GM_Curve");
 A   DROP INDEX public."dancu_curve_congtrinhcongnghiep_GM_Curve_id";
       public            postgres    false    276    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2                       1259    84069 '   dancu_curve_congtrinhphutro_GM_Curve_id    INDEX     v   CREATE INDEX "dancu_curve_congtrinhphutro_GM_Curve_id" ON public.dancu_curve_congtrinhphutro USING gist ("GM_Curve");
 =   DROP INDEX public."dancu_curve_congtrinhphutro_GM_Curve_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    238                       1259    84068 4   dancu_curve_congtrinhphutro_maNhanDang_e44ee656_like    INDEX     �   CREATE INDEX "dancu_curve_congtrinhphutro_maNhanDang_e44ee656_like" ON public.dancu_curve_congtrinhphutro USING btree (manhandang varchar_pattern_ops);
 J   DROP INDEX public."dancu_curve_congtrinhphutro_maNhanDang_e44ee656_like";
       public            postgres    false    238                       1259    84071    dancu_diadanhdancu_GM_Point_id    INDEX     d   CREATE INDEX "dancu_diadanhdancu_GM_Point_id" ON public.dancu_diadanhdancu USING gist ("GM_Point");
 4   DROP INDEX public."dancu_diadanhdancu_GM_Point_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    239                       1259    84070 +   dancu_diadanhdancu_maNhanDang_568b3a48_like    INDEX     �   CREATE INDEX "dancu_diadanhdancu_maNhanDang_568b3a48_like" ON public.dancu_diadanhdancu USING btree (manhandang varchar_pattern_ops);
 A   DROP INDEX public."dancu_diadanhdancu_maNhanDang_568b3a48_like";
       public            postgres    false    239                       1259    84073 !   dancu_duongdaytaidien_GM_Curve_id    INDEX     j   CREATE INDEX "dancu_duongdaytaidien_GM_Curve_id" ON public.dancu_duongdaytaidien USING gist ("GM_Curve");
 7   DROP INDEX public."dancu_duongdaytaidien_GM_Curve_id";
       public            postgres    false    240    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2                       1259    84072 .   dancu_duongdaytaidien_maNhanDang_18d55778_like    INDEX     �   CREATE INDEX "dancu_duongdaytaidien_maNhanDang_18d55778_like" ON public.dancu_duongdaytaidien USING btree (manhandang varchar_pattern_ops);
 D   DROP INDEX public."dancu_duongdaytaidien_maNhanDang_18d55778_like";
       public            postgres    false    240                        1259    84075    dancu_duongongdan_GM_Curve_id    INDEX     b   CREATE INDEX "dancu_duongongdan_GM_Curve_id" ON public.dancu_duongongdan USING gist ("GM_Curve");
 3   DROP INDEX public."dancu_duongongdan_GM_Curve_id";
       public            postgres    false    241    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2            !           1259    84074 *   dancu_duongongdan_maNhanDang_7584dee7_like    INDEX     �   CREATE INDEX "dancu_duongongdan_maNhanDang_7584dee7_like" ON public.dancu_duongongdan USING btree (manhandang varchar_pattern_ops);
 @   DROP INDEX public."dancu_duongongdan_maNhanDang_7584dee7_like";
       public            postgres    false    241            $           1259    84077    dancu_khoinha_GM_Surface_id    INDEX     ^   CREATE INDEX "dancu_khoinha_GM_Surface_id" ON public.dancu_khoinha USING gist ("GM_Surface");
 1   DROP INDEX public."dancu_khoinha_GM_Surface_id";
       public            postgres    false    242    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2            %           1259    84076 &   dancu_khoinha_maNhanDang_2383414b_like    INDEX     |   CREATE INDEX "dancu_khoinha_maNhanDang_2383414b_like" ON public.dancu_khoinha USING btree (manhandang varchar_pattern_ops);
 <   DROP INDEX public."dancu_khoinha_maNhanDang_2383414b_like";
       public            postgres    false    242            (           1259    84079 %   dancu_khuchucnangdacthu_GM_Surface_id    INDEX     r   CREATE INDEX "dancu_khuchucnangdacthu_GM_Surface_id" ON public.dancu_khuchucnangdacthu USING gist ("GM_Surface");
 ;   DROP INDEX public."dancu_khuchucnangdacthu_GM_Surface_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    243            )           1259    84078 0   dancu_khuchucnangdacthu_maNhanDang_9311c946_like    INDEX     �   CREATE INDEX "dancu_khuchucnangdacthu_maNhanDang_9311c946_like" ON public.dancu_khuchucnangdacthu USING btree (manhandang varchar_pattern_ops);
 F   DROP INDEX public."dancu_khuchucnangdacthu_maNhanDang_9311c946_like";
       public            postgres    false    243            ,           1259    84081    dancu_khudancu_GM_Surface_id    INDEX     `   CREATE INDEX "dancu_khudancu_GM_Surface_id" ON public.dancu_khudancu USING gist ("GM_Surface");
 2   DROP INDEX public."dancu_khudancu_GM_Surface_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    244            -           1259    84080 '   dancu_khudancu_maNhanDang_2fa3b99d_like    INDEX     ~   CREATE INDEX "dancu_khudancu_maNhanDang_2fa3b99d_like" ON public.dancu_khudancu USING btree (manhandang varchar_pattern_ops);
 =   DROP INDEX public."dancu_khudancu_maNhanDang_2fa3b99d_like";
       public            postgres    false    244            0           1259    84083 '   dancu_point_congtrinhanninh_GM_Point_id    INDEX     v   CREATE INDEX "dancu_point_congtrinhanninh_GM_Point_id" ON public.dancu_point_congtrinhanninh USING gist ("GM_Point");
 =   DROP INDEX public."dancu_point_congtrinhanninh_GM_Point_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    245            1           1259    84082 4   dancu_point_congtrinhanninh_maNhanDang_45f7525c_like    INDEX     �   CREATE INDEX "dancu_point_congtrinhanninh_maNhanDang_45f7525c_like" ON public.dancu_point_congtrinhanninh USING btree (manhandang varchar_pattern_ops);
 J   DROP INDEX public."dancu_point_congtrinhanninh_maNhanDang_45f7525c_like";
       public            postgres    false    245            �           1259    84156 ?   dancu_point_congtrinhcon_congtrinhcongnghiep_ptr__5ca14438_like    INDEX     �   CREATE INDEX dancu_point_congtrinhcon_congtrinhcongnghiep_ptr__5ca14438_like ON public.dancu_point_congtrinhcongnghiep USING btree (congtrinhcongnghiep_ptr_id varchar_pattern_ops);
 S   DROP INDEX public.dancu_point_congtrinhcon_congtrinhcongnghiep_ptr__5ca14438_like;
       public            postgres    false    277            �           1259    84157 +   dancu_point_congtrinhcongnghiep_GM_Point_id    INDEX     ~   CREATE INDEX "dancu_point_congtrinhcongnghiep_GM_Point_id" ON public.dancu_point_congtrinhcongnghiep USING gist ("GM_Point");
 A   DROP INDEX public."dancu_point_congtrinhcongnghiep_GM_Point_id";
       public            postgres    false    277    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2            4           1259    84085 (   dancu_point_congtrinhgiaoduc_GM_Point_id    INDEX     x   CREATE INDEX "dancu_point_congtrinhgiaoduc_GM_Point_id" ON public.dancu_point_congtrinhgiaoduc USING gist ("GM_Point");
 >   DROP INDEX public."dancu_point_congtrinhgiaoduc_GM_Point_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    246            5           1259    84084 5   dancu_point_congtrinhgiaoduc_maNhanDang_1511c57c_like    INDEX     �   CREATE INDEX "dancu_point_congtrinhgiaoduc_maNhanDang_1511c57c_like" ON public.dancu_point_congtrinhgiaoduc USING btree (manhandang varchar_pattern_ops);
 K   DROP INDEX public."dancu_point_congtrinhgiaoduc_maNhanDang_1511c57c_like";
       public            postgres    false    246            8           1259    84087 *   dancu_point_congtrinhquocphong_GM_Point_id    INDEX     |   CREATE INDEX "dancu_point_congtrinhquocphong_GM_Point_id" ON public.dancu_point_congtrinhquocphong USING gist ("GM_Point");
 @   DROP INDEX public."dancu_point_congtrinhquocphong_GM_Point_id";
       public            postgres    false    247    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2            9           1259    84086 7   dancu_point_congtrinhquocphong_maNhanDang_e9ed6dcf_like    INDEX     �   CREATE INDEX "dancu_point_congtrinhquocphong_maNhanDang_e9ed6dcf_like" ON public.dancu_point_congtrinhquocphong USING btree (manhandang varchar_pattern_ops);
 M   DROP INDEX public."dancu_point_congtrinhquocphong_maNhanDang_e9ed6dcf_like";
       public            postgres    false    247            <           1259    84089 (   dancu_point_congtrinhthethao_GM_Point_id    INDEX     x   CREATE INDEX "dancu_point_congtrinhthethao_GM_Point_id" ON public.dancu_point_congtrinhthethao USING gist ("GM_Point");
 >   DROP INDEX public."dancu_point_congtrinhthethao_GM_Point_id";
       public            postgres    false    248    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2            =           1259    84088 5   dancu_point_congtrinhthethao_maNhanDang_d5f5e855_like    INDEX     �   CREATE INDEX "dancu_point_congtrinhthethao_maNhanDang_d5f5e855_like" ON public.dancu_point_congtrinhthethao USING btree (manhandang varchar_pattern_ops);
 K   DROP INDEX public."dancu_point_congtrinhthethao_maNhanDang_d5f5e855_like";
       public            postgres    false    248            @           1259    84091 0   dancu_point_congtrinhthuongmaidichvu_GM_Point_id    INDEX     �   CREATE INDEX "dancu_point_congtrinhthuongmaidichvu_GM_Point_id" ON public.dancu_point_congtrinhthuongmaidichvu USING gist ("GM_Point");
 F   DROP INDEX public."dancu_point_congtrinhthuongmaidichvu_GM_Point_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    249            A           1259    84090 =   dancu_point_congtrinhthuongmaidichvu_maNhanDang_8bf18042_like    INDEX     �   CREATE INDEX "dancu_point_congtrinhthuongmaidichvu_maNhanDang_8bf18042_like" ON public.dancu_point_congtrinhthuongmaidichvu USING btree (manhandang varchar_pattern_ops);
 S   DROP INDEX public."dancu_point_congtrinhthuongmaidichvu_maNhanDang_8bf18042_like";
       public            postgres    false    249            D           1259    84093 1   dancu_point_congtrinhtongiaotinnguong_GM_Point_id    INDEX     �   CREATE INDEX "dancu_point_congtrinhtongiaotinnguong_GM_Point_id" ON public.dancu_point_congtrinhtongiaotinnguong USING gist ("GM_Point");
 G   DROP INDEX public."dancu_point_congtrinhtongiaotinnguong_GM_Point_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    250            E           1259    84092 >   dancu_point_congtrinhtongiaotinnguong_maNhanDang_6eb557a4_like    INDEX     �   CREATE INDEX "dancu_point_congtrinhtongiaotinnguong_maNhanDang_6eb557a4_like" ON public.dancu_point_congtrinhtongiaotinnguong USING btree (manhandang varchar_pattern_ops);
 T   DROP INDEX public."dancu_point_congtrinhtongiaotinnguong_maNhanDang_6eb557a4_like";
       public            postgres    false    250            H           1259    84095 '   dancu_point_congtrinhvanhoa_GM_Point_id    INDEX     v   CREATE INDEX "dancu_point_congtrinhvanhoa_GM_Point_id" ON public.dancu_point_congtrinhvanhoa USING gist ("GM_Point");
 =   DROP INDEX public."dancu_point_congtrinhvanhoa_GM_Point_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    251            I           1259    84094 4   dancu_point_congtrinhvanhoa_maNhanDang_6b7ac413_like    INDEX     �   CREATE INDEX "dancu_point_congtrinhvanhoa_maNhanDang_6b7ac413_like" ON public.dancu_point_congtrinhvanhoa USING btree (manhandang varchar_pattern_ops);
 J   DROP INDEX public."dancu_point_congtrinhvanhoa_maNhanDang_6b7ac413_like";
       public            postgres    false    251            L           1259    84097 -   dancu_point_congtrinhxulychatthai_GM_Point_id    INDEX     �   CREATE INDEX "dancu_point_congtrinhxulychatthai_GM_Point_id" ON public.dancu_point_congtrinhxulychatthai USING gist ("GM_Point");
 C   DROP INDEX public."dancu_point_congtrinhxulychatthai_GM_Point_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    252            M           1259    84096 :   dancu_point_congtrinhxulychatthai_maNhanDang_fce16e43_like    INDEX     �   CREATE INDEX "dancu_point_congtrinhxulychatthai_maNhanDang_fce16e43_like" ON public.dancu_point_congtrinhxulychatthai USING btree (manhandang varchar_pattern_ops);
 P   DROP INDEX public."dancu_point_congtrinhxulychatthai_maNhanDang_fce16e43_like";
       public            postgres    false    252            P           1259    84099 $   dancu_point_congtrinhyte_GM_Point_id    INDEX     p   CREATE INDEX "dancu_point_congtrinhyte_GM_Point_id" ON public.dancu_point_congtrinhyte USING gist ("GM_Point");
 :   DROP INDEX public."dancu_point_congtrinhyte_GM_Point_id";
       public            postgres    false    253    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2            Q           1259    84098 1   dancu_point_congtrinhyte_maNhanDang_02554566_like    INDEX     �   CREATE INDEX "dancu_point_congtrinhyte_maNhanDang_02554566_like" ON public.dancu_point_congtrinhyte USING btree (manhandang varchar_pattern_ops);
 G   DROP INDEX public."dancu_point_congtrinhyte_maNhanDang_02554566_like";
       public            postgres    false    253            T           1259    84101 0   dancu_point_cososanxuatnonglamnghiep_GM_Point_id    INDEX     �   CREATE INDEX "dancu_point_cososanxuatnonglamnghiep_GM_Point_id" ON public.dancu_point_cososanxuatnonglamnghiep USING gist ("GM_Point");
 F   DROP INDEX public."dancu_point_cososanxuatnonglamnghiep_GM_Point_id";
       public            postgres    false    254    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2            U           1259    84100 =   dancu_point_cososanxuatnonglamnghiep_maNhanDang_f1f7d114_like    INDEX     �   CREATE INDEX "dancu_point_cososanxuatnonglamnghiep_maNhanDang_f1f7d114_like" ON public.dancu_point_cososanxuatnonglamnghiep USING btree (manhandang varchar_pattern_ops);
 S   DROP INDEX public."dancu_point_cososanxuatnonglamnghiep_maNhanDang_f1f7d114_like";
       public            postgres    false    254            X           1259    84103 )   dancu_point_hatangkythuatkhac_GM_Point_id    INDEX     z   CREATE INDEX "dancu_point_hatangkythuatkhac_GM_Point_id" ON public.dancu_point_hatangkythuatkhac USING gist ("GM_Point");
 ?   DROP INDEX public."dancu_point_hatangkythuatkhac_GM_Point_id";
       public            postgres    false    255    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2            Y           1259    84102 6   dancu_point_hatangkythuatkhac_maNhanDang_19f59364_like    INDEX     �   CREATE INDEX "dancu_point_hatangkythuatkhac_maNhanDang_19f59364_like" ON public.dancu_point_hatangkythuatkhac USING btree (manhandang varchar_pattern_ops);
 L   DROP INDEX public."dancu_point_hatangkythuatkhac_maNhanDang_19f59364_like";
       public            postgres    false    255            \           1259    84105    dancu_point_nha_GM_Point_id    INDEX     ^   CREATE INDEX "dancu_point_nha_GM_Point_id" ON public.dancu_point_nha USING gist ("GM_Point");
 1   DROP INDEX public."dancu_point_nha_GM_Point_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    256            ]           1259    84104 (   dancu_point_nha_maNhanDang_b1b93cd9_like    INDEX     �   CREATE INDEX "dancu_point_nha_maNhanDang_b1b93cd9_like" ON public.dancu_point_nha USING btree (manhandang varchar_pattern_ops);
 >   DROP INDEX public."dancu_point_nha_maNhanDang_b1b93cd9_like";
       public            postgres    false    256            `           1259    84107 *   dancu_point_trusocoquannhanuoc_GM_Point_id    INDEX     |   CREATE INDEX "dancu_point_trusocoquannhanuoc_GM_Point_id" ON public.dancu_point_trusocoquannhanuoc USING gist ("GM_Point");
 @   DROP INDEX public."dancu_point_trusocoquannhanuoc_GM_Point_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    257            a           1259    84106 7   dancu_point_trusocoquannhanuoc_maNhanDang_f3be3ea2_like    INDEX     �   CREATE INDEX "dancu_point_trusocoquannhanuoc_maNhanDang_f3be3ea2_like" ON public.dancu_point_trusocoquannhanuoc USING btree (manhandang varchar_pattern_ops);
 M   DROP INDEX public."dancu_point_trusocoquannhanuoc_maNhanDang_f3be3ea2_like";
       public            postgres    false    257            d           1259    84109    dancu_ranhgioi_GM_Curve_id    INDEX     \   CREATE INDEX "dancu_ranhgioi_GM_Curve_id" ON public.dancu_ranhgioi USING gist ("GM_Curve");
 0   DROP INDEX public."dancu_ranhgioi_GM_Curve_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    258            e           1259    84108 '   dancu_ranhgioi_maNhanDang_6790dbb4_like    INDEX     ~   CREATE INDEX "dancu_ranhgioi_maNhanDang_6790dbb4_like" ON public.dancu_ranhgioi USING btree (manhandang varchar_pattern_ops);
 =   DROP INDEX public."dancu_ranhgioi_maNhanDang_6790dbb4_like";
       public            postgres    false    258            h           1259    84111 +   dancu_surface_congtrinhanninh_GM_Surface_id    INDEX     ~   CREATE INDEX "dancu_surface_congtrinhanninh_GM_Surface_id" ON public.dancu_surface_congtrinhanninh USING gist ("GM_Surface");
 A   DROP INDEX public."dancu_surface_congtrinhanninh_GM_Surface_id";
       public            postgres    false    259    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2            i           1259    84110 6   dancu_surface_congtrinhanninh_maNhanDang_14412af0_like    INDEX     �   CREATE INDEX "dancu_surface_congtrinhanninh_maNhanDang_14412af0_like" ON public.dancu_surface_congtrinhanninh USING btree (manhandang varchar_pattern_ops);
 L   DROP INDEX public."dancu_surface_congtrinhanninh_maNhanDang_14412af0_like";
       public            postgres    false    259            �           1259    84163 ?   dancu_surface_congtrinhc_congtrinhcongnghiep_ptr__91d937a2_like    INDEX     �   CREATE INDEX dancu_surface_congtrinhc_congtrinhcongnghiep_ptr__91d937a2_like ON public.dancu_surface_congtrinhcongnghiep USING btree (congtrinhcongnghiep_ptr_id varchar_pattern_ops);
 S   DROP INDEX public.dancu_surface_congtrinhc_congtrinhcongnghiep_ptr__91d937a2_like;
       public            postgres    false    278            �           1259    84164 /   dancu_surface_congtrinhcongnghiep_GM_Surface_id    INDEX     �   CREATE INDEX "dancu_surface_congtrinhcongnghiep_GM_Surface_id" ON public.dancu_surface_congtrinhcongnghiep USING gist ("GM_Surface");
 E   DROP INDEX public."dancu_surface_congtrinhcongnghiep_GM_Surface_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    278            l           1259    84113 ,   dancu_surface_congtrinhgiaoduc_GM_Surface_id    INDEX     �   CREATE INDEX "dancu_surface_congtrinhgiaoduc_GM_Surface_id" ON public.dancu_surface_congtrinhgiaoduc USING gist ("GM_Surface");
 B   DROP INDEX public."dancu_surface_congtrinhgiaoduc_GM_Surface_id";
       public            postgres    false    260    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2            m           1259    84112 7   dancu_surface_congtrinhgiaoduc_maNhanDang_fe9da18e_like    INDEX     �   CREATE INDEX "dancu_surface_congtrinhgiaoduc_maNhanDang_fe9da18e_like" ON public.dancu_surface_congtrinhgiaoduc USING btree (manhandang varchar_pattern_ops);
 M   DROP INDEX public."dancu_surface_congtrinhgiaoduc_maNhanDang_fe9da18e_like";
       public            postgres    false    260            p           1259    84115 +   dancu_surface_congtrinhphutro_GM_Surface_id    INDEX     ~   CREATE INDEX "dancu_surface_congtrinhphutro_GM_Surface_id" ON public.dancu_surface_congtrinhphutro USING gist ("GM_Surface");
 A   DROP INDEX public."dancu_surface_congtrinhphutro_GM_Surface_id";
       public            postgres    false    261    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2            q           1259    84114 6   dancu_surface_congtrinhphutro_maNhanDang_6d77b110_like    INDEX     �   CREATE INDEX "dancu_surface_congtrinhphutro_maNhanDang_6d77b110_like" ON public.dancu_surface_congtrinhphutro USING btree (manhandang varchar_pattern_ops);
 L   DROP INDEX public."dancu_surface_congtrinhphutro_maNhanDang_6d77b110_like";
       public            postgres    false    261            t           1259    84117 .   dancu_surface_congtrinhquocphong_GM_Surface_id    INDEX     �   CREATE INDEX "dancu_surface_congtrinhquocphong_GM_Surface_id" ON public.dancu_surface_congtrinhquocphong USING gist ("GM_Surface");
 D   DROP INDEX public."dancu_surface_congtrinhquocphong_GM_Surface_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    262            u           1259    84116 9   dancu_surface_congtrinhquocphong_maNhanDang_ffa02f13_like    INDEX     �   CREATE INDEX "dancu_surface_congtrinhquocphong_maNhanDang_ffa02f13_like" ON public.dancu_surface_congtrinhquocphong USING btree (manhandang varchar_pattern_ops);
 O   DROP INDEX public."dancu_surface_congtrinhquocphong_maNhanDang_ffa02f13_like";
       public            postgres    false    262            �           1259    84122 1   dancu_surface_congtrinht_maNhanDang_4143f1a8_like    INDEX     �   CREATE INDEX "dancu_surface_congtrinht_maNhanDang_4143f1a8_like" ON public.dancu_surface_congtrinhtongiaotinnguong USING btree (manhandang varchar_pattern_ops);
 G   DROP INDEX public."dancu_surface_congtrinht_maNhanDang_4143f1a8_like";
       public            postgres    false    265            x           1259    84119 ,   dancu_surface_congtrinhthethao_GM_Surface_id    INDEX     �   CREATE INDEX "dancu_surface_congtrinhthethao_GM_Surface_id" ON public.dancu_surface_congtrinhthethao USING gist ("GM_Surface");
 B   DROP INDEX public."dancu_surface_congtrinhthethao_GM_Surface_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    263            y           1259    84118 7   dancu_surface_congtrinhthethao_maNhanDang_991f7a6d_like    INDEX     �   CREATE INDEX "dancu_surface_congtrinhthethao_maNhanDang_991f7a6d_like" ON public.dancu_surface_congtrinhthethao USING btree (manhandang varchar_pattern_ops);
 M   DROP INDEX public."dancu_surface_congtrinhthethao_maNhanDang_991f7a6d_like";
       public            postgres    false    263            |           1259    84121 4   dancu_surface_congtrinhthuongmaidichvu_GM_Surface_id    INDEX     �   CREATE INDEX "dancu_surface_congtrinhthuongmaidichvu_GM_Surface_id" ON public.dancu_surface_congtrinhthuongmaidichvu USING gist ("GM_Surface");
 J   DROP INDEX public."dancu_surface_congtrinhthuongmaidichvu_GM_Surface_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    264            }           1259    84120 ?   dancu_surface_congtrinhthuongmaidichvu_maNhanDang_59f71f6e_like    INDEX     �   CREATE INDEX "dancu_surface_congtrinhthuongmaidichvu_maNhanDang_59f71f6e_like" ON public.dancu_surface_congtrinhthuongmaidichvu USING btree (manhandang varchar_pattern_ops);
 U   DROP INDEX public."dancu_surface_congtrinhthuongmaidichvu_maNhanDang_59f71f6e_like";
       public            postgres    false    264            �           1259    84123 5   dancu_surface_congtrinhtongiaotinnguong_GM_Surface_id    INDEX     �   CREATE INDEX "dancu_surface_congtrinhtongiaotinnguong_GM_Surface_id" ON public.dancu_surface_congtrinhtongiaotinnguong USING gist ("GM_Surface");
 K   DROP INDEX public."dancu_surface_congtrinhtongiaotinnguong_GM_Surface_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    265            �           1259    84125 +   dancu_surface_congtrinhvanhoa_GM_Surface_id    INDEX     ~   CREATE INDEX "dancu_surface_congtrinhvanhoa_GM_Surface_id" ON public.dancu_surface_congtrinhvanhoa USING gist ("GM_Surface");
 A   DROP INDEX public."dancu_surface_congtrinhvanhoa_GM_Surface_id";
       public            postgres    false    266    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2            �           1259    84124 6   dancu_surface_congtrinhvanhoa_maNhanDang_304788de_like    INDEX     �   CREATE INDEX "dancu_surface_congtrinhvanhoa_maNhanDang_304788de_like" ON public.dancu_surface_congtrinhvanhoa USING btree (manhandang varchar_pattern_ops);
 L   DROP INDEX public."dancu_surface_congtrinhvanhoa_maNhanDang_304788de_like";
       public            postgres    false    266            �           1259    84127 1   dancu_surface_congtrinhxulychatthai_GM_Surface_id    INDEX     �   CREATE INDEX "dancu_surface_congtrinhxulychatthai_GM_Surface_id" ON public.dancu_surface_congtrinhxulychatthai USING gist ("GM_Surface");
 G   DROP INDEX public."dancu_surface_congtrinhxulychatthai_GM_Surface_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    267            �           1259    84126 <   dancu_surface_congtrinhxulychatthai_maNhanDang_6d20bdc2_like    INDEX     �   CREATE INDEX "dancu_surface_congtrinhxulychatthai_maNhanDang_6d20bdc2_like" ON public.dancu_surface_congtrinhxulychatthai USING btree (manhandang varchar_pattern_ops);
 R   DROP INDEX public."dancu_surface_congtrinhxulychatthai_maNhanDang_6d20bdc2_like";
       public            postgres    false    267            �           1259    84129 (   dancu_surface_congtrinhyte_GM_Surface_id    INDEX     x   CREATE INDEX "dancu_surface_congtrinhyte_GM_Surface_id" ON public.dancu_surface_congtrinhyte USING gist ("GM_Surface");
 >   DROP INDEX public."dancu_surface_congtrinhyte_GM_Surface_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    268            �           1259    84128 3   dancu_surface_congtrinhyte_maNhanDang_66124ea1_like    INDEX     �   CREATE INDEX "dancu_surface_congtrinhyte_maNhanDang_66124ea1_like" ON public.dancu_surface_congtrinhyte USING btree (manhandang varchar_pattern_ops);
 I   DROP INDEX public."dancu_surface_congtrinhyte_maNhanDang_66124ea1_like";
       public            postgres    false    268            �           1259    84131 4   dancu_surface_cososanxuatnonglamnghiep_GM_Surface_id    INDEX     �   CREATE INDEX "dancu_surface_cososanxuatnonglamnghiep_GM_Surface_id" ON public.dancu_surface_cososanxuatnonglamnghiep USING gist ("GM_Surface");
 J   DROP INDEX public."dancu_surface_cososanxuatnonglamnghiep_GM_Surface_id";
       public            postgres    false    269    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2            �           1259    84130 ?   dancu_surface_cososanxuatnonglamnghiep_maNhanDang_1340b72c_like    INDEX     �   CREATE INDEX "dancu_surface_cososanxuatnonglamnghiep_maNhanDang_1340b72c_like" ON public.dancu_surface_cososanxuatnonglamnghiep USING btree (manhandang varchar_pattern_ops);
 U   DROP INDEX public."dancu_surface_cososanxuatnonglamnghiep_maNhanDang_1340b72c_like";
       public            postgres    false    269            �           1259    84133 -   dancu_surface_hatangkythuatkhac_GM_Surface_id    INDEX     �   CREATE INDEX "dancu_surface_hatangkythuatkhac_GM_Surface_id" ON public.dancu_surface_hatangkythuatkhac USING gist ("GM_Surface");
 C   DROP INDEX public."dancu_surface_hatangkythuatkhac_GM_Surface_id";
       public            postgres    false    270    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2            �           1259    84132 8   dancu_surface_hatangkythuatkhac_maNhanDang_3f5242f0_like    INDEX     �   CREATE INDEX "dancu_surface_hatangkythuatkhac_maNhanDang_3f5242f0_like" ON public.dancu_surface_hatangkythuatkhac USING btree (manhandang varchar_pattern_ops);
 N   DROP INDEX public."dancu_surface_hatangkythuatkhac_maNhanDang_3f5242f0_like";
       public            postgres    false    270            �           1259    84135    dancu_surface_nha_GM_Surface_id    INDEX     f   CREATE INDEX "dancu_surface_nha_GM_Surface_id" ON public.dancu_surface_nha USING gist ("GM_Surface");
 5   DROP INDEX public."dancu_surface_nha_GM_Surface_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    271            �           1259    84134 *   dancu_surface_nha_maNhanDang_d2419ca5_like    INDEX     �   CREATE INDEX "dancu_surface_nha_maNhanDang_d2419ca5_like" ON public.dancu_surface_nha USING btree (manhandang varchar_pattern_ops);
 @   DROP INDEX public."dancu_surface_nha_maNhanDang_d2419ca5_like";
       public            postgres    false    271            �           1259    84137 .   dancu_surface_trusocoquannhanuoc_GM_Surface_id    INDEX     �   CREATE INDEX "dancu_surface_trusocoquannhanuoc_GM_Surface_id" ON public.dancu_surface_trusocoquannhanuoc USING gist ("GM_Surface");
 D   DROP INDEX public."dancu_surface_trusocoquannhanuoc_GM_Surface_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    272            �           1259    84136 9   dancu_surface_trusocoquannhanuoc_maNhanDang_dcaeea93_like    INDEX     �   CREATE INDEX "dancu_surface_trusocoquannhanuoc_maNhanDang_dcaeea93_like" ON public.dancu_surface_trusocoquannhanuoc USING btree (manhandang varchar_pattern_ops);
 O   DROP INDEX public."dancu_surface_trusocoquannhanuoc_maNhanDang_dcaeea93_like";
       public            postgres    false    272            �           1259    84139 .   dancu_tramkhituongthuyvanquocgia_GM_Surface_id    INDEX     �   CREATE INDEX "dancu_tramkhituongthuyvanquocgia_GM_Surface_id" ON public.dancu_tramkhituongthuyvanquocgia USING gist ("GM_Surface");
 D   DROP INDEX public."dancu_tramkhituongthuyvanquocgia_GM_Surface_id";
       public            postgres    false    273    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2            �           1259    84138 9   dancu_tramkhituongthuyvanquocgia_maNhanDang_06c50374_like    INDEX     �   CREATE INDEX "dancu_tramkhituongthuyvanquocgia_maNhanDang_06c50374_like" ON public.dancu_tramkhituongthuyvanquocgia USING btree (manhandang varchar_pattern_ops);
 O   DROP INDEX public."dancu_tramkhituongthuyvanquocgia_maNhanDang_06c50374_like";
       public            postgres    false    273            �           1259    84141 )   dancu_tramquantracmoitruong_GM_Surface_id    INDEX     z   CREATE INDEX "dancu_tramquantracmoitruong_GM_Surface_id" ON public.dancu_tramquantracmoitruong USING gist ("GM_Surface");
 ?   DROP INDEX public."dancu_tramquantracmoitruong_GM_Surface_id";
       public            postgres    false    274    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2            �           1259    84140 4   dancu_tramquantracmoitruong_maNhanDang_36fd6b6a_like    INDEX     �   CREATE INDEX "dancu_tramquantracmoitruong_maNhanDang_36fd6b6a_like" ON public.dancu_tramquantracmoitruong USING btree (manhandang varchar_pattern_ops);
 J   DROP INDEX public."dancu_tramquantracmoitruong_maNhanDang_36fd6b6a_like";
       public            postgres    false    274            �           1259    84143 -   dancu_tramquantractainguyennuoc_GM_Surface_id    INDEX     �   CREATE INDEX "dancu_tramquantractainguyennuoc_GM_Surface_id" ON public.dancu_tramquantractainguyennuoc USING gist ("GM_Surface");
 C   DROP INDEX public."dancu_tramquantractainguyennuoc_GM_Surface_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    275            �           1259    84142 8   dancu_tramquantractainguyennuoc_maNhanDang_9a190db0_like    INDEX     �   CREATE INDEX "dancu_tramquantractainguyennuoc_maNhanDang_9a190db0_like" ON public.dancu_tramquantractainguyennuoc USING btree (manhandang varchar_pattern_ops);
 N   DROP INDEX public."dancu_tramquantractainguyennuoc_maNhanDang_9a190db0_like";
       public            postgres    false    275            �           1259    84297    diahinh_chatday_GM_Point_id    INDEX     ^   CREATE INDEX "diahinh_chatday_GM_Point_id" ON public.diahinh_chatday USING gist ("GM_Point");
 1   DROP INDEX public."diahinh_chatday_GM_Point_id";
       public            postgres    false    279    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2            �           1259    84296 (   diahinh_chatday_maNhanDang_1d05f6a7_like    INDEX     �   CREATE INDEX "diahinh_chatday_maNhanDang_1d05f6a7_like" ON public.diahinh_chatday USING btree (manhandang varchar_pattern_ops);
 >   DROP INDEX public."diahinh_chatday_maNhanDang_1d05f6a7_like";
       public            postgres    false    279            �           1259    84299 /   diahinh_curve_diahinhdacbietdaybien_GM_Curve_id    INDEX     �   CREATE INDEX "diahinh_curve_diahinhdacbietdaybien_GM_Curve_id" ON public.diahinh_curve_diahinhdacbietdaybien USING gist ("GM_Curve");
 E   DROP INDEX public."diahinh_curve_diahinhdacbietdaybien_GM_Curve_id";
       public            postgres    false    280    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2            �           1259    84298 <   diahinh_curve_diahinhdacbietdaybien_maNhanDang_9b2179b8_like    INDEX     �   CREATE INDEX "diahinh_curve_diahinhdacbietdaybien_maNhanDang_9b2179b8_like" ON public.diahinh_curve_diahinhdacbietdaybien USING btree (manhandang varchar_pattern_ops);
 R   DROP INDEX public."diahinh_curve_diahinhdacbietdaybien_maNhanDang_9b2179b8_like";
       public            postgres    false    280            �           1259    84301    diahinh_diamao_GM_Surface_id    INDEX     `   CREATE INDEX "diahinh_diamao_GM_Surface_id" ON public.diahinh_diamao USING gist ("GM_Surface");
 2   DROP INDEX public."diahinh_diamao_GM_Surface_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    281            �           1259    84300 '   diahinh_diamao_maNhanDang_6f261ce4_like    INDEX     ~   CREATE INDEX "diahinh_diamao_maNhanDang_6f261ce4_like" ON public.diahinh_diamao USING btree (manhandang varchar_pattern_ops);
 =   DROP INDEX public."diahinh_diamao_maNhanDang_6f261ce4_like";
       public            postgres    false    281            �           1259    84303    diahinh_diemdocao_GM_Point_id    INDEX     b   CREATE INDEX "diahinh_diemdocao_GM_Point_id" ON public.diahinh_diemdocao USING gist ("GM_Point");
 3   DROP INDEX public."diahinh_diemdocao_GM_Point_id";
       public            postgres    false    282    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2            �           1259    84302 *   diahinh_diemdocao_maNhanDang_5513b838_like    INDEX     �   CREATE INDEX "diahinh_diemdocao_maNhanDang_5513b838_like" ON public.diahinh_diemdocao USING btree (manhandang varchar_pattern_ops);
 @   DROP INDEX public."diahinh_diemdocao_maNhanDang_5513b838_like";
       public            postgres    false    282            �           1259    84305    diahinh_diemdosau_GM_Point_id    INDEX     b   CREATE INDEX "diahinh_diemdosau_GM_Point_id" ON public.diahinh_diemdosau USING gist ("GM_Point");
 3   DROP INDEX public."diahinh_diemdosau_GM_Point_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    283            �           1259    84304 *   diahinh_diemdosau_maNhanDang_2a519546_like    INDEX     �   CREATE INDEX "diahinh_diemdosau_maNhanDang_2a519546_like" ON public.diahinh_diemdosau USING btree (manhandang varchar_pattern_ops);
 @   DROP INDEX public."diahinh_diemdosau_maNhanDang_2a519546_like";
       public            postgres    false    283            �           1259    84307    diahinh_duongbinhdo_GM_Curve_id    INDEX     f   CREATE INDEX "diahinh_duongbinhdo_GM_Curve_id" ON public.diahinh_duongbinhdo USING gist ("GM_Curve");
 5   DROP INDEX public."diahinh_duongbinhdo_GM_Curve_id";
       public            postgres    false    284    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2            �           1259    84306 ,   diahinh_duongbinhdo_maNhanDang_fb431205_like    INDEX     �   CREATE INDEX "diahinh_duongbinhdo_maNhanDang_fb431205_like" ON public.diahinh_duongbinhdo USING btree (manhandang varchar_pattern_ops);
 B   DROP INDEX public."diahinh_duongbinhdo_maNhanDang_fb431205_like";
       public            postgres    false    284            �           1259    84309 "   diahinh_duongbinhdosau_GM_Curve_id    INDEX     l   CREATE INDEX "diahinh_duongbinhdosau_GM_Curve_id" ON public.diahinh_duongbinhdosau USING gist ("GM_Curve");
 8   DROP INDEX public."diahinh_duongbinhdosau_GM_Curve_id";
       public            postgres    false    285    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2            �           1259    84308 /   diahinh_duongbinhdosau_maNhanDang_15f2dad2_like    INDEX     �   CREATE INDEX "diahinh_duongbinhdosau_maNhanDang_15f2dad2_like" ON public.diahinh_duongbinhdosau USING btree (manhandang varchar_pattern_ops);
 E   DROP INDEX public."diahinh_duongbinhdosau_maNhanDang_15f2dad2_like";
       public            postgres    false    285            �           1259    84311 "   diahinh_hokhoandiachat_GM_Point_id    INDEX     l   CREATE INDEX "diahinh_hokhoandiachat_GM_Point_id" ON public.diahinh_hokhoandiachat USING gist ("GM_Point");
 8   DROP INDEX public."diahinh_hokhoandiachat_GM_Point_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    286            �           1259    84310 /   diahinh_hokhoandiachat_maNhanDang_4dad161f_like    INDEX     �   CREATE INDEX "diahinh_hokhoandiachat_maNhanDang_4dad161f_like" ON public.diahinh_hokhoandiachat USING btree (manhandang varchar_pattern_ops);
 E   DROP INDEX public."diahinh_hokhoandiachat_maNhanDang_4dad161f_like";
       public            postgres    false    286            �           1259    84313 !   diahinh_loaidiachat_GM_Surface_id    INDEX     j   CREATE INDEX "diahinh_loaidiachat_GM_Surface_id" ON public.diahinh_loaidiachat USING gist ("GM_Surface");
 7   DROP INDEX public."diahinh_loaidiachat_GM_Surface_id";
       public            postgres    false    287    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2            �           1259    84312 ,   diahinh_loaidiachat_maNhanDang_d9952712_like    INDEX     �   CREATE INDEX "diahinh_loaidiachat_maNhanDang_d9952712_like" ON public.diahinh_loaidiachat USING btree (manhandang varchar_pattern_ops);
 B   DROP INDEX public."diahinh_loaidiachat_maNhanDang_d9952712_like";
       public            postgres    false    287            �           1259    84315 "   diahinh_matcatdienhinh_GM_Curve_id    INDEX     l   CREATE INDEX "diahinh_matcatdienhinh_GM_Curve_id" ON public.diahinh_matcatdienhinh USING gist ("GM_Curve");
 8   DROP INDEX public."diahinh_matcatdienhinh_GM_Curve_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    288            �           1259    84314 /   diahinh_matcatdienhinh_maNhanDang_c75e1d53_like    INDEX     �   CREATE INDEX "diahinh_matcatdienhinh_maNhanDang_c75e1d53_like" ON public.diahinh_matcatdienhinh USING btree (manhandang varchar_pattern_ops);
 E   DROP INDEX public."diahinh_matcatdienhinh_maNhanDang_c75e1d53_like";
       public            postgres    false    288            �           1259    84317 +   diahinh_mohinhsodocaogoclopdiem_GM_Point_id    INDEX     ~   CREATE INDEX "diahinh_mohinhsodocaogoclopdiem_GM_Point_id" ON public.diahinh_mohinhsodocaogoclopdiem USING gist ("GM_Point");
 A   DROP INDEX public."diahinh_mohinhsodocaogoclopdiem_GM_Point_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    289            �           1259    84316 8   diahinh_mohinhsodocaogoclopdiem_maNhanDang_9d588d8b_like    INDEX     �   CREATE INDEX "diahinh_mohinhsodocaogoclopdiem_maNhanDang_9d588d8b_like" ON public.diahinh_mohinhsodocaogoclopdiem USING btree (manhandang varchar_pattern_ops);
 N   DROP INDEX public."diahinh_mohinhsodocaogoclopdiem_maNhanDang_9d588d8b_like";
       public            postgres    false    289            �           1259    84319 ,   diahinh_mohinhsodocaogoclopduong_GM_Curve_id    INDEX     �   CREATE INDEX "diahinh_mohinhsodocaogoclopduong_GM_Curve_id" ON public.diahinh_mohinhsodocaogoclopduong USING gist ("GM_Curve");
 B   DROP INDEX public."diahinh_mohinhsodocaogoclopduong_GM_Curve_id";
       public            postgres    false    290    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2            �           1259    84318 9   diahinh_mohinhsodocaogoclopduong_maNhanDang_679e0fa5_like    INDEX     �   CREATE INDEX "diahinh_mohinhsodocaogoclopduong_maNhanDang_679e0fa5_like" ON public.diahinh_mohinhsodocaogoclopduong USING btree (manhandang varchar_pattern_ops);
 O   DROP INDEX public."diahinh_mohinhsodocaogoclopduong_maNhanDang_679e0fa5_like";
       public            postgres    false    290            �           1259    84321 -   diahinh_mohinhsodocaogoclopvung_GM_Surface_id    INDEX     �   CREATE INDEX "diahinh_mohinhsodocaogoclopvung_GM_Surface_id" ON public.diahinh_mohinhsodocaogoclopvung USING gist ("GM_Surface");
 C   DROP INDEX public."diahinh_mohinhsodocaogoclopvung_GM_Surface_id";
       public            postgres    false    291    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2            �           1259    84320 8   diahinh_mohinhsodocaogoclopvung_maNhanDang_699aa317_like    INDEX     �   CREATE INDEX "diahinh_mohinhsodocaogoclopvung_maNhanDang_699aa317_like" ON public.diahinh_mohinhsodocaogoclopvung USING btree (manhandang varchar_pattern_ops);
 N   DROP INDEX public."diahinh_mohinhsodocaogoclopvung_maNhanDang_699aa317_like";
       public            postgres    false    291            �           1259    84323 4   diahinh_mohinhsodocaogoclopvungbientap_GM_Surface_id    INDEX     �   CREATE INDEX "diahinh_mohinhsodocaogoclopvungbientap_GM_Surface_id" ON public.diahinh_mohinhsodocaogoclopvungbientap USING gist ("GM_Surface");
 J   DROP INDEX public."diahinh_mohinhsodocaogoclopvungbientap_GM_Surface_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    292            �           1259    84322 ?   diahinh_mohinhsodocaogoclopvungbientap_maNhanDang_99784fb7_like    INDEX     �   CREATE INDEX "diahinh_mohinhsodocaogoclopvungbientap_maNhanDang_99784fb7_like" ON public.diahinh_mohinhsodocaogoclopvungbientap USING btree (manhandang varchar_pattern_ops);
 U   DROP INDEX public."diahinh_mohinhsodocaogoclopvungbientap_maNhanDang_99784fb7_like";
       public            postgres    false    292            �           1259    84331 #   diahinh_solieuhkdc_HKDC_id_5a8d313c    INDEX     i   CREATE INDEX "diahinh_solieuhkdc_HKDC_id_5a8d313c" ON public.diahinh_solieuhkdc USING btree ("HKDC_id");
 9   DROP INDEX public."diahinh_solieuhkdc_HKDC_id_5a8d313c";
       public            postgres    false    295            �           1259    84332 (   diahinh_solieuhkdc_HKDC_id_5a8d313c_like    INDEX     �   CREATE INDEX "diahinh_solieuhkdc_HKDC_id_5a8d313c_like" ON public.diahinh_solieuhkdc USING btree ("HKDC_id" varchar_pattern_ops);
 >   DROP INDEX public."diahinh_solieuhkdc_HKDC_id_5a8d313c_like";
       public            postgres    false    295            �           1259    84325 3   diahinh_surface_diahinhdacbietdaybien_GM_Surface_id    INDEX     �   CREATE INDEX "diahinh_surface_diahinhdacbietdaybien_GM_Surface_id" ON public.diahinh_surface_diahinhdacbietdaybien USING gist ("GM_Surface");
 I   DROP INDEX public."diahinh_surface_diahinhdacbietdaybien_GM_Surface_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    293            �           1259    84324 >   diahinh_surface_diahinhdacbietdaybien_maNhanDang_69ee9f40_like    INDEX     �   CREATE INDEX "diahinh_surface_diahinhdacbietdaybien_maNhanDang_69ee9f40_like" ON public.diahinh_surface_diahinhdacbietdaybien USING btree (manhandang varchar_pattern_ops);
 T   DROP INDEX public."diahinh_surface_diahinhdacbietdaybien_maNhanDang_69ee9f40_like";
       public            postgres    false    293            �           1259    83642 )   django_admin_log_content_type_id_c4bce8eb    INDEX     q   CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);
 =   DROP INDEX public.django_admin_log_content_type_id_c4bce8eb;
       public            postgres    false    228            �           1259    83648 !   django_admin_log_user_id_c564eba6    INDEX     a   CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);
 5   DROP INDEX public.django_admin_log_user_id_c564eba6;
       public            postgres    false    228            �           1259    84754 #   django_session_expire_date_a5c62663    INDEX     e   CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);
 7   DROP INDEX public.django_session_expire_date_a5c62663;
       public            postgres    false    335            �           1259    84753 (   django_session_session_key_c0390e0f_like    INDEX     ~   CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);
 <   DROP INDEX public.django_session_session_key_c0390e0f_like;
       public            postgres    false    335            �           1259    83581 .   dulieuquantri_bienchetrangbi_donVi_id_b4f1eda2    INDEX        CREATE INDEX "dulieuquantri_bienchetrangbi_donVi_id_b4f1eda2" ON public.dulieuquantri_bienchetrangbi USING btree ("donVi_id");
 D   DROP INDEX public."dulieuquantri_bienchetrangbi_donVi_id_b4f1eda2";
       public            postgres    false    212            �           1259    83582 3   dulieuquantri_bienchetrangbi_donVi_id_b4f1eda2_like    INDEX     �   CREATE INDEX "dulieuquantri_bienchetrangbi_donVi_id_b4f1eda2_like" ON public.dulieuquantri_bienchetrangbi USING btree ("donVi_id" varchar_pattern_ops);
 I   DROP INDEX public."dulieuquantri_bienchetrangbi_donVi_id_b4f1eda2_like";
       public            postgres    false    212            �           1259    83583 4   dulieuquantri_bienchetrangbi_loaiTrangBi_id_00af7f77    INDEX     �   CREATE INDEX "dulieuquantri_bienchetrangbi_loaiTrangBi_id_00af7f77" ON public.dulieuquantri_bienchetrangbi USING btree ("loaiTrangBiKhiTai_id");
 J   DROP INDEX public."dulieuquantri_bienchetrangbi_loaiTrangBi_id_00af7f77";
       public            postgres    false    212            �           1259    83584 9   dulieuquantri_bienchetrangbi_loaiTrangBi_id_00af7f77_like    INDEX     �   CREATE INDEX "dulieuquantri_bienchetrangbi_loaiTrangBi_id_00af7f77_like" ON public.dulieuquantri_bienchetrangbi USING btree ("loaiTrangBiKhiTai_id" varchar_pattern_ops);
 O   DROP INDEX public."dulieuquantri_bienchetrangbi_loaiTrangBi_id_00af7f77_like";
       public            postgres    false    212            �           1259    83532 5   dulieuquantri_bienchetrangbi_maNhanDang_d67fd090_like    INDEX     �   CREATE INDEX "dulieuquantri_bienchetrangbi_maNhanDang_d67fd090_like" ON public.dulieuquantri_bienchetrangbi USING btree ("maNhanDang" varchar_pattern_ops);
 K   DROP INDEX public."dulieuquantri_bienchetrangbi_maNhanDang_d67fd090_like";
       public            postgres    false    212            �           1259    83585 4   dulieuquantri_bienchetrangbi_tinhTrangTB_id_76368f17    INDEX     �   CREATE INDEX "dulieuquantri_bienchetrangbi_tinhTrangTB_id_76368f17" ON public.dulieuquantri_bienchetrangbi USING btree ("tinhTrangTrangBi_id");
 J   DROP INDEX public."dulieuquantri_bienchetrangbi_tinhTrangTB_id_76368f17";
       public            postgres    false    212            �           1259    83586 9   dulieuquantri_bienchetrangbi_tinhTrangTB_id_76368f17_like    INDEX     �   CREATE INDEX "dulieuquantri_bienchetrangbi_tinhTrangTB_id_76368f17_like" ON public.dulieuquantri_bienchetrangbi USING btree ("tinhTrangTrangBi_id" varchar_pattern_ops);
 O   DROP INDEX public."dulieuquantri_bienchetrangbi_tinhTrangTB_id_76368f17_like";
       public            postgres    false    212            �           1259    83587 /   dulieuquantri_bienchetrangbi_xuatXu_id_d700e72f    INDEX     �   CREATE INDEX "dulieuquantri_bienchetrangbi_xuatXu_id_d700e72f" ON public.dulieuquantri_bienchetrangbi USING btree ("xuatXu_id");
 E   DROP INDEX public."dulieuquantri_bienchetrangbi_xuatXu_id_d700e72f";
       public            postgres    false    212            �           1259    83588 4   dulieuquantri_bienchetrangbi_xuatXu_id_d700e72f_like    INDEX     �   CREATE INDEX "dulieuquantri_bienchetrangbi_xuatXu_id_d700e72f_like" ON public.dulieuquantri_bienchetrangbi USING btree ("xuatXu_id" varchar_pattern_ops);
 J   DROP INDEX public."dulieuquantri_bienchetrangbi_xuatXu_id_d700e72f_like";
       public            postgres    false    212            �           1259    83533 /   dulieuquantri_capdonvi_maNhanDang_aefd1d97_like    INDEX     �   CREATE INDEX "dulieuquantri_capdonvi_maNhanDang_aefd1d97_like" ON public.dulieuquantri_capdonvi USING btree ("maNhanDang" varchar_pattern_ops);
 E   DROP INDEX public."dulieuquantri_capdonvi_maNhanDang_aefd1d97_like";
       public            postgres    false    213            �           1259    85628 $   dulieuquantri_donvi_CTQP_id_32ca9ea7    INDEX     k   CREATE INDEX "dulieuquantri_donvi_CTQP_id_32ca9ea7" ON public.dulieuquantri_donvi USING btree ("CTQP_id");
 :   DROP INDEX public."dulieuquantri_donvi_CTQP_id_32ca9ea7";
       public            postgres    false    220            �           1259    85629 )   dulieuquantri_donvi_CTQP_id_32ca9ea7_like    INDEX     �   CREATE INDEX "dulieuquantri_donvi_CTQP_id_32ca9ea7_like" ON public.dulieuquantri_donvi USING btree ("CTQP_id" varchar_pattern_ops);
 ?   DROP INDEX public."dulieuquantri_donvi_CTQP_id_32ca9ea7_like";
       public            postgres    false    220            �           1259    83577 (   dulieuquantri_donvi_capDonVi_id_7bae2bf4    INDEX     s   CREATE INDEX "dulieuquantri_donvi_capDonVi_id_7bae2bf4" ON public.dulieuquantri_donvi USING btree ("capDonVi_id");
 >   DROP INDEX public."dulieuquantri_donvi_capDonVi_id_7bae2bf4";
       public            postgres    false    220            �           1259    83578 -   dulieuquantri_donvi_capDonVi_id_7bae2bf4_like    INDEX     �   CREATE INDEX "dulieuquantri_donvi_capDonVi_id_7bae2bf4_like" ON public.dulieuquantri_donvi USING btree ("capDonVi_id" varchar_pattern_ops);
 C   DROP INDEX public."dulieuquantri_donvi_capDonVi_id_7bae2bf4_like";
       public            postgres    false    220            �           1259    83579 )   dulieuquantri_donvi_loaiDonVi_id_83857109    INDEX     u   CREATE INDEX "dulieuquantri_donvi_loaiDonVi_id_83857109" ON public.dulieuquantri_donvi USING btree ("loaiDonVi_id");
 ?   DROP INDEX public."dulieuquantri_donvi_loaiDonVi_id_83857109";
       public            postgres    false    220            �           1259    83580 .   dulieuquantri_donvi_loaiDonVi_id_83857109_like    INDEX     �   CREATE INDEX "dulieuquantri_donvi_loaiDonVi_id_83857109_like" ON public.dulieuquantri_donvi USING btree ("loaiDonVi_id" varchar_pattern_ops);
 D   DROP INDEX public."dulieuquantri_donvi_loaiDonVi_id_83857109_like";
       public            postgres    false    220            �           1259    83576 ,   dulieuquantri_donvi_maNhanDang_7ab231ac_like    INDEX     �   CREATE INDEX "dulieuquantri_donvi_maNhanDang_7ab231ac_like" ON public.dulieuquantri_donvi USING btree ("maNhanDang" varchar_pattern_ops);
 B   DROP INDEX public."dulieuquantri_donvi_maNhanDang_7ab231ac_like";
       public            postgres    false    220            �           1259    83549 0   dulieuquantri_loaidonvi_maNhanDang_9008e7f6_like    INDEX     �   CREATE INDEX "dulieuquantri_loaidonvi_maNhanDang_9008e7f6_like" ON public.dulieuquantri_loaidonvi USING btree ("maNhanDang" varchar_pattern_ops);
 F   DROP INDEX public."dulieuquantri_loaidonvi_maNhanDang_9008e7f6_like";
       public            postgres    false    214            �           1259    83550 2   dulieuquantri_loaitrangbi_maNhanDang_dc7966d3_like    INDEX     �   CREATE INDEX "dulieuquantri_loaitrangbi_maNhanDang_dc7966d3_like" ON public.dulieuquantri_loaitrangbikhitai USING btree ("maNhanDang" varchar_pattern_ops);
 H   DROP INDEX public."dulieuquantri_loaitrangbi_maNhanDang_dc7966d3_like";
       public            postgres    false    215            �           1259    83595 )   dulieuquantri_nguoidung_donVi_id_96e959e6    INDEX     u   CREATE INDEX "dulieuquantri_nguoidung_donVi_id_96e959e6" ON public.dulieuquantri_nguoidung USING btree ("donVi_id");
 ?   DROP INDEX public."dulieuquantri_nguoidung_donVi_id_96e959e6";
       public            postgres    false    222            �           1259    83596 .   dulieuquantri_nguoidung_donVi_id_96e959e6_like    INDEX     �   CREATE INDEX "dulieuquantri_nguoidung_donVi_id_96e959e6_like" ON public.dulieuquantri_nguoidung USING btree ("donVi_id" varchar_pattern_ops);
 D   DROP INDEX public."dulieuquantri_nguoidung_donVi_id_96e959e6_like";
       public            postgres    false    222            �           1259    83610 0   dulieuquantri_nguoidung_groups_group_id_d858ede1    INDEX        CREATE INDEX dulieuquantri_nguoidung_groups_group_id_d858ede1 ON public.dulieuquantri_nguoidung_groups USING btree (group_id);
 D   DROP INDEX public.dulieuquantri_nguoidung_groups_group_id_d858ede1;
       public            postgres    false    224            �           1259    83609 4   dulieuquantri_nguoidung_groups_nguoidung_id_347564d5    INDEX     �   CREATE INDEX dulieuquantri_nguoidung_groups_nguoidung_id_347564d5 ON public.dulieuquantri_nguoidung_groups USING btree (nguoidung_id);
 H   DROP INDEX public.dulieuquantri_nguoidung_groups_nguoidung_id_347564d5;
       public            postgres    false    224            �           1259    83623 >   dulieuquantri_nguoidung_user_permissions_nguoidung_id_4a884827    INDEX     �   CREATE INDEX dulieuquantri_nguoidung_user_permissions_nguoidung_id_4a884827 ON public.dulieuquantri_nguoidung_user_permissions USING btree (nguoidung_id);
 R   DROP INDEX public.dulieuquantri_nguoidung_user_permissions_nguoidung_id_4a884827;
       public            postgres    false    226            �           1259    83624 ?   dulieuquantri_nguoidung_user_permissions_permission_id_4f784da8    INDEX     �   CREATE INDEX dulieuquantri_nguoidung_user_permissions_permission_id_4f784da8 ON public.dulieuquantri_nguoidung_user_permissions USING btree (permission_id);
 S   DROP INDEX public.dulieuquantri_nguoidung_user_permissions_permission_id_4f784da8;
       public            postgres    false    226            �           1259    83594 .   dulieuquantri_nguoidung_username_9b7f9d85_like    INDEX     �   CREATE INDEX dulieuquantri_nguoidung_username_9b7f9d85_like ON public.dulieuquantri_nguoidung USING btree (username varchar_pattern_ops);
 B   DROP INDEX public.dulieuquantri_nguoidung_username_9b7f9d85_like;
       public            postgres    false    222            H           1259    91859 1   dulieuquantri_thietbikhitai_bienCheTB_id_9721a570    INDEX     �   CREATE INDEX "dulieuquantri_thietbikhitai_bienCheTB_id_9721a570" ON public.dulieuquantri_thietbikhitai USING btree ("bienCheTB_id");
 G   DROP INDEX public."dulieuquantri_thietbikhitai_bienCheTB_id_9721a570";
       public            postgres    false    380            I           1259    91860 6   dulieuquantri_thietbikhitai_bienCheTB_id_9721a570_like    INDEX     �   CREATE INDEX "dulieuquantri_thietbikhitai_bienCheTB_id_9721a570_like" ON public.dulieuquantri_thietbikhitai USING btree ("bienCheTB_id" varchar_pattern_ops);
 L   DROP INDEX public."dulieuquantri_thietbikhitai_bienCheTB_id_9721a570_like";
       public            postgres    false    380            J           1259    91861 9   dulieuquantri_thietbikhitai_loaiTrangBiKhiTai_id_0dd84a5c    INDEX     �   CREATE INDEX "dulieuquantri_thietbikhitai_loaiTrangBiKhiTai_id_0dd84a5c" ON public.dulieuquantri_thietbikhitai USING btree ("loaiTrangBiKhiTai_id");
 O   DROP INDEX public."dulieuquantri_thietbikhitai_loaiTrangBiKhiTai_id_0dd84a5c";
       public            postgres    false    380            K           1259    91862 >   dulieuquantri_thietbikhitai_loaiTrangBiKhiTai_id_0dd84a5c_like    INDEX     �   CREATE INDEX "dulieuquantri_thietbikhitai_loaiTrangBiKhiTai_id_0dd84a5c_like" ON public.dulieuquantri_thietbikhitai USING btree ("loaiTrangBiKhiTai_id" varchar_pattern_ops);
 T   DROP INDEX public."dulieuquantri_thietbikhitai_loaiTrangBiKhiTai_id_0dd84a5c_like";
       public            postgres    false    380            L           1259    91858 4   dulieuquantri_thietbikhitai_maNhanDang_d47c72c3_like    INDEX     �   CREATE INDEX "dulieuquantri_thietbikhitai_maNhanDang_d47c72c3_like" ON public.dulieuquantri_thietbikhitai USING btree ("maNhanDang" varchar_pattern_ops);
 J   DROP INDEX public."dulieuquantri_thietbikhitai_maNhanDang_d47c72c3_like";
       public            postgres    false    380            O           1259    91863 8   dulieuquantri_thietbikhitai_tinhTrangTrangBi_id_d012e038    INDEX     �   CREATE INDEX "dulieuquantri_thietbikhitai_tinhTrangTrangBi_id_d012e038" ON public.dulieuquantri_thietbikhitai USING btree ("tinhTrangTrangBi_id");
 N   DROP INDEX public."dulieuquantri_thietbikhitai_tinhTrangTrangBi_id_d012e038";
       public            postgres    false    380            P           1259    91864 =   dulieuquantri_thietbikhitai_tinhTrangTrangBi_id_d012e038_like    INDEX     �   CREATE INDEX "dulieuquantri_thietbikhitai_tinhTrangTrangBi_id_d012e038_like" ON public.dulieuquantri_thietbikhitai USING btree ("tinhTrangTrangBi_id" varchar_pattern_ops);
 S   DROP INDEX public."dulieuquantri_thietbikhitai_tinhTrangTrangBi_id_d012e038_like";
       public            postgres    false    380            Q           1259    91865 .   dulieuquantri_thietbikhitai_xuatXu_id_3f8b8ee6    INDEX        CREATE INDEX "dulieuquantri_thietbikhitai_xuatXu_id_3f8b8ee6" ON public.dulieuquantri_thietbikhitai USING btree ("xuatXu_id");
 D   DROP INDEX public."dulieuquantri_thietbikhitai_xuatXu_id_3f8b8ee6";
       public            postgres    false    380            R           1259    91866 3   dulieuquantri_thietbikhitai_xuatXu_id_3f8b8ee6_like    INDEX     �   CREATE INDEX "dulieuquantri_thietbikhitai_xuatXu_id_3f8b8ee6_like" ON public.dulieuquantri_thietbikhitai USING btree ("xuatXu_id" varchar_pattern_ops);
 I   DROP INDEX public."dulieuquantri_thietbikhitai_xuatXu_id_3f8b8ee6_like";
       public            postgres    false    380            �           1259    83551 7   dulieuquantri_tinhtrangtrangbi_maNhanDang_4b2a64b0_like    INDEX     �   CREATE INDEX "dulieuquantri_tinhtrangtrangbi_maNhanDang_4b2a64b0_like" ON public.dulieuquantri_tinhtrangtrangbi USING btree ("maNhanDang" varchar_pattern_ops);
 M   DROP INDEX public."dulieuquantri_tinhtrangtrangbi_maNhanDang_4b2a64b0_like";
       public            postgres    false    216            �           1259    83552 -   dulieuquantri_xuatxu_maNhanDang_da687f9d_like    INDEX     �   CREATE INDEX "dulieuquantri_xuatxu_maNhanDang_da687f9d_like" ON public.dulieuquantri_xuatxu USING btree ("maNhanDang" varchar_pattern_ops);
 C   DROP INDEX public."dulieuquantri_xuatxu_maNhanDang_da687f9d_like";
       public            postgres    false    217            �           1259    84409 -   eav_attribute_entity_ct_attribute_id_384edb80    INDEX     y   CREATE INDEX eav_attribute_entity_ct_attribute_id_384edb80 ON public.eav_attribute_entity_ct USING btree (attribute_id);
 A   DROP INDEX public.eav_attribute_entity_ct_attribute_id_384edb80;
       public            postgres    false    299                       1259    84410 /   eav_attribute_entity_ct_contenttype_id_6a747efe    INDEX     }   CREATE INDEX eav_attribute_entity_ct_contenttype_id_6a747efe ON public.eav_attribute_entity_ct USING btree (contenttype_id);
 C   DROP INDEX public.eav_attribute_entity_ct_contenttype_id_6a747efe;
       public            postgres    false    299            �           1259    84451 $   eav_attribute_enum_group_id_47628614    INDEX     g   CREATE INDEX eav_attribute_enum_group_id_47628614 ON public.eav_attribute USING btree (enum_group_id);
 8   DROP INDEX public.eav_attribute_enum_group_id_47628614;
       public            postgres    false    297            �           1259    84396     eav_attribute_slug_1c525d06_like    INDEX     n   CREATE INDEX eav_attribute_slug_1c525d06_like ON public.eav_attribute USING btree (slug varchar_pattern_ops);
 4   DROP INDEX public.eav_attribute_slug_1c525d06_like;
       public            postgres    false    297                       1259    84436     eav_enumgroup_name_1077d89b_like    INDEX     n   CREATE INDEX eav_enumgroup_name_1077d89b_like ON public.eav_enumgroup USING btree (name varchar_pattern_ops);
 4   DROP INDEX public.eav_enumgroup_name_1077d89b_like;
       public            postgres    false    305                       1259    84449 *   eav_enumgroup_values_enumgroup_id_2bdd7858    INDEX     s   CREATE INDEX eav_enumgroup_values_enumgroup_id_2bdd7858 ON public.eav_enumgroup_values USING btree (enumgroup_id);
 >   DROP INDEX public.eav_enumgroup_values_enumgroup_id_2bdd7858;
       public            postgres    false    307                       1259    84450 *   eav_enumgroup_values_enumvalue_id_52f83e3a    INDEX     s   CREATE INDEX eav_enumgroup_values_enumvalue_id_52f83e3a ON public.eav_enumgroup_values USING btree (enumvalue_id);
 >   DROP INDEX public.eav_enumgroup_values_enumvalue_id_52f83e3a;
       public            postgres    false    307                       1259    84411 !   eav_enumvalue_value_027e7652_like    INDEX     p   CREATE INDEX eav_enumvalue_value_027e7652_like ON public.eav_enumvalue USING btree (value varchar_pattern_ops);
 5   DROP INDEX public.eav_enumvalue_value_027e7652_like;
       public            postgres    false    301            	           1259    84432    eav_value_attribute_id_6fd472ba    INDEX     ]   CREATE INDEX eav_value_attribute_id_6fd472ba ON public.eav_value USING btree (attribute_id);
 3   DROP INDEX public.eav_value_attribute_id_6fd472ba;
       public            postgres    false    303            
           1259    84433    eav_value_entity_ct_id_5cfd530e    INDEX     ]   CREATE INDEX eav_value_entity_ct_id_5cfd530e ON public.eav_value USING btree (entity_ct_id);
 3   DROP INDEX public.eav_value_entity_ct_id_5cfd530e;
       public            postgres    false    303                       1259    84434 &   eav_value_generic_value_ct_id_d4681436    INDEX     k   CREATE INDEX eav_value_generic_value_ct_id_d4681436 ON public.eav_value USING btree (generic_value_ct_id);
 :   DROP INDEX public.eav_value_generic_value_ct_id_d4681436;
       public            postgres    false    303                       1259    84435     eav_value_value_enum_id_86e48f74    INDEX     _   CREATE INDEX eav_value_value_enum_id_86e48f74 ON public.eav_value USING btree (value_enum_id);
 4   DROP INDEX public.eav_value_value_enum_id_86e48f74;
       public            postgres    false    303                       1259    84565 '   giaothong_baidaptructhang_GM_Surface_id    INDEX     v   CREATE INDEX "giaothong_baidaptructhang_GM_Surface_id" ON public.giaothong_baidaptructhang USING gist ("GM_Surface");
 =   DROP INDEX public."giaothong_baidaptructhang_GM_Surface_id";
       public            postgres    false    308    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2                       1259    84564 2   giaothong_baidaptructhang_maNhanDang_f0504faf_like    INDEX     �   CREATE INDEX "giaothong_baidaptructhang_maNhanDang_f0504faf_like" ON public.giaothong_baidaptructhang USING btree (manhandang varchar_pattern_ops);
 H   DROP INDEX public."giaothong_baidaptructhang_maNhanDang_f0504faf_like";
       public            postgres    false    308                       1259    84566 1   giaothong_baohieudanluon_maNhanDang_53228dc6_like    INDEX     �   CREATE INDEX "giaothong_baohieudanluon_maNhanDang_53228dc6_like" ON public.giaothong_baohieudanluonghanghaiduongthuy USING btree (manhandang varchar_pattern_ops);
 G   DROP INDEX public."giaothong_baohieudanluon_maNhanDang_53228dc6_like";
       public            postgres    false    309                       1259    84567 5   giaothong_baohieudanluonghanghaiduongthuy_GM_Point_id    INDEX     �   CREATE INDEX "giaothong_baohieudanluonghanghaiduongthuy_GM_Point_id" ON public.giaothong_baohieudanluonghanghaiduongthuy USING gist ("GM_Point");
 K   DROP INDEX public."giaothong_baohieudanluonghanghaiduongthuy_GM_Point_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    309            "           1259    84569 '   giaothong_baohieuhanghaiais_GM_Point_id    INDEX     v   CREATE INDEX "giaothong_baohieuhanghaiais_GM_Point_id" ON public.giaothong_baohieuhanghaiais USING gist ("GM_Point");
 =   DROP INDEX public."giaothong_baohieuhanghaiais_GM_Point_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    310            #           1259    84568 4   giaothong_baohieuhanghaiais_maNhanDang_27524723_like    INDEX     �   CREATE INDEX "giaothong_baohieuhanghaiais_maNhanDang_27524723_like" ON public.giaothong_baohieuhanghaiais USING btree (manhandang varchar_pattern_ops);
 J   DROP INDEX public."giaothong_baohieuhanghaiais_maNhanDang_27524723_like";
       public            postgres    false    310            &           1259    84571    giaothong_bencang_GM_Surface_id    INDEX     f   CREATE INDEX "giaothong_bencang_GM_Surface_id" ON public.giaothong_bencang USING gist ("GM_Surface");
 5   DROP INDEX public."giaothong_bencang_GM_Surface_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    311            '           1259    84570 *   giaothong_bencang_maNhanDang_97122b0b_like    INDEX     �   CREATE INDEX "giaothong_bencang_maNhanDang_97122b0b_like" ON public.giaothong_bencang USING btree (manhandang varchar_pattern_ops);
 @   DROP INDEX public."giaothong_bencang_maNhanDang_97122b0b_like";
       public            postgres    false    311            *           1259    84573 "   giaothong_curve_cautau_GM_Curve_id    INDEX     l   CREATE INDEX "giaothong_curve_cautau_GM_Curve_id" ON public.giaothong_curve_cautau USING gist ("GM_Curve");
 8   DROP INDEX public."giaothong_curve_cautau_GM_Curve_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    312            +           1259    84572 /   giaothong_curve_cautau_maNhanDang_bb1dff0d_like    INDEX     �   CREATE INDEX "giaothong_curve_cautau_maNhanDang_bb1dff0d_like" ON public.giaothong_curve_cautau USING btree (manhandang varchar_pattern_ops);
 E   DROP INDEX public."giaothong_curve_cautau_maNhanDang_bb1dff0d_like";
       public            postgres    false    312            .           1259    84575 )   giaothong_curve_conggiaothong_GM_Curve_id    INDEX     z   CREATE INDEX "giaothong_curve_conggiaothong_GM_Curve_id" ON public.giaothong_curve_conggiaothong USING gist ("GM_Curve");
 ?   DROP INDEX public."giaothong_curve_conggiaothong_GM_Curve_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    313            /           1259    84574 6   giaothong_curve_conggiaothong_maNhanDang_2f88966e_like    INDEX     �   CREATE INDEX "giaothong_curve_conggiaothong_maNhanDang_2f88966e_like" ON public.giaothong_curve_conggiaothong USING btree (manhandang varchar_pattern_ops);
 L   DROP INDEX public."giaothong_curve_conggiaothong_maNhanDang_2f88966e_like";
       public            postgres    false    313            2           1259    84577 %   giaothong_curve_nhomautau_GM_Curve_id    INDEX     r   CREATE INDEX "giaothong_curve_nhomautau_GM_Curve_id" ON public.giaothong_curve_nhomautau USING gist ("GM_Curve");
 ;   DROP INDEX public."giaothong_curve_nhomautau_GM_Curve_id";
       public            postgres    false    314    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2            3           1259    84576 2   giaothong_curve_nhomautau_maNhanDang_86cfaf6c_like    INDEX     �   CREATE INDEX "giaothong_curve_nhomautau_maNhanDang_86cfaf6c_like" ON public.giaothong_curve_nhomautau USING btree (manhandang varchar_pattern_ops);
 H   DROP INDEX public."giaothong_curve_nhomautau_maNhanDang_86cfaf6c_like";
       public            postgres    false    314            6           1259    84579 !   giaothong_duongbang_GM_Surface_id    INDEX     j   CREATE INDEX "giaothong_duongbang_GM_Surface_id" ON public.giaothong_duongbang USING gist ("GM_Surface");
 7   DROP INDEX public."giaothong_duongbang_GM_Surface_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    315            7           1259    84578 ,   giaothong_duongbang_maNhanDang_c22926d6_like    INDEX     �   CREATE INDEX "giaothong_duongbang_maNhanDang_c22926d6_like" ON public.giaothong_duongbang USING btree (manhandang varchar_pattern_ops);
 B   DROP INDEX public."giaothong_duongbang_maNhanDang_c22926d6_like";
       public            postgres    false    315            :           1259    84581    giaothong_duongbo_GM_Curve_id    INDEX     b   CREATE INDEX "giaothong_duongbo_GM_Curve_id" ON public.giaothong_duongbo USING gist ("GM_Curve");
 3   DROP INDEX public."giaothong_duongbo_GM_Curve_id";
       public            postgres    false    316    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2            ;           1259    84580 *   giaothong_duongbo_maNhanDang_0d0f108d_like    INDEX     �   CREATE INDEX "giaothong_duongbo_maNhanDang_0d0f108d_like" ON public.giaothong_duongbo USING btree (manhandang varchar_pattern_ops);
 @   DROP INDEX public."giaothong_duongbo_maNhanDang_0d0f108d_like";
       public            postgres    false    316            >           1259    84582 1   giaothong_point_cacdoitu_maNhanDang_26ac7ca9_like    INDEX     �   CREATE INDEX "giaothong_point_cacdoitu_maNhanDang_26ac7ca9_like" ON public.giaothong_point_cacdoituonghanghaihaivan USING btree (manhandang varchar_pattern_ops);
 G   DROP INDEX public."giaothong_point_cacdoitu_maNhanDang_26ac7ca9_like";
       public            postgres    false    317            ?           1259    84583 4   giaothong_point_cacdoituonghanghaihaivan_GM_Point_id    INDEX     �   CREATE INDEX "giaothong_point_cacdoituonghanghaihaivan_GM_Point_id" ON public.giaothong_point_cacdoituonghanghaihaivan USING gist ("GM_Point");
 J   DROP INDEX public."giaothong_point_cacdoituonghanghaihaivan_GM_Point_id";
       public            postgres    false    317    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2            B           1259    84585 )   giaothong_point_conggiaothong_GM_Point_id    INDEX     z   CREATE INDEX "giaothong_point_conggiaothong_GM_Point_id" ON public.giaothong_point_conggiaothong USING gist ("GM_Point");
 ?   DROP INDEX public."giaothong_point_conggiaothong_GM_Point_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    318            C           1259    84584 6   giaothong_point_conggiaothong_maNhanDang_925270e0_like    INDEX     �   CREATE INDEX "giaothong_point_conggiaothong_maNhanDang_925270e0_like" ON public.giaothong_point_conggiaothong USING btree (manhandang varchar_pattern_ops);
 L   DROP INDEX public."giaothong_point_conggiaothong_maNhanDang_925270e0_like";
       public            postgres    false    318            F           1259    84586 1   giaothong_surface_cacdoi_maNhanDang_54e94b3b_like    INDEX     �   CREATE INDEX "giaothong_surface_cacdoi_maNhanDang_54e94b3b_like" ON public.giaothong_surface_cacdoituonghanghaihaivan USING btree (manhandang varchar_pattern_ops);
 G   DROP INDEX public."giaothong_surface_cacdoi_maNhanDang_54e94b3b_like";
       public            postgres    false    319            G           1259    84587 8   giaothong_surface_cacdoituonghanghaihaivan_GM_Surface_id    INDEX     �   CREATE INDEX "giaothong_surface_cacdoituonghanghaihaivan_GM_Surface_id" ON public.giaothong_surface_cacdoituonghanghaihaivan USING gist ("GM_Surface");
 N   DROP INDEX public."giaothong_surface_cacdoituonghanghaihaivan_GM_Surface_id";
       public            postgres    false    319    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2            J           1259    84589 &   giaothong_surface_cautau_GM_Surface_id    INDEX     t   CREATE INDEX "giaothong_surface_cautau_GM_Surface_id" ON public.giaothong_surface_cautau USING gist ("GM_Surface");
 <   DROP INDEX public."giaothong_surface_cautau_GM_Surface_id";
       public            postgres    false    320    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2            K           1259    84588 1   giaothong_surface_cautau_maNhanDang_499644e2_like    INDEX     �   CREATE INDEX "giaothong_surface_cautau_maNhanDang_499644e2_like" ON public.giaothong_surface_cautau USING btree (manhandang varchar_pattern_ops);
 G   DROP INDEX public."giaothong_surface_cautau_maNhanDang_499644e2_like";
       public            postgres    false    320            N           1259    84591 )   giaothong_surface_nhomautau_GM_Surface_id    INDEX     z   CREATE INDEX "giaothong_surface_nhomautau_GM_Surface_id" ON public.giaothong_surface_nhomautau USING gist ("GM_Surface");
 ?   DROP INDEX public."giaothong_surface_nhomautau_GM_Surface_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    321            O           1259    84590 4   giaothong_surface_nhomautau_maNhanDang_e7a714fe_like    INDEX     �   CREATE INDEX "giaothong_surface_nhomautau_maNhanDang_e7a714fe_like" ON public.giaothong_surface_nhomautau USING btree (manhandang varchar_pattern_ops);
 J   DROP INDEX public."giaothong_surface_nhomautau_maNhanDang_e7a714fe_like";
       public            postgres    false    321            k           1259    85594 /   multimedia_dulieudaphuongtien_maLop_id_faf7c5dc    INDEX     �   CREATE INDEX "multimedia_dulieudaphuongtien_maLop_id_faf7c5dc" ON public.multimedia_dulieudaphuongtien USING btree ("lopDL_id");
 E   DROP INDEX public."multimedia_dulieudaphuongtien_maLop_id_faf7c5dc";
       public            postgres    false    327            l           1259    85595 4   multimedia_dulieudaphuongtien_maLop_id_faf7c5dc_like    INDEX     �   CREATE INDEX "multimedia_dulieudaphuongtien_maLop_id_faf7c5dc_like" ON public.multimedia_dulieudaphuongtien USING btree ("lopDL_id" varchar_pattern_ops);
 J   DROP INDEX public."multimedia_dulieudaphuongtien_maLop_id_faf7c5dc_like";
       public            postgres    false    327            m           1259    84672 6   multimedia_dulieudaphuongtien_maNhanDang_dcc76de2_like    INDEX     �   CREATE INDEX "multimedia_dulieudaphuongtien_maNhanDang_dcc76de2_like" ON public.multimedia_dulieudaphuongtien USING btree ("maNhanDang" varchar_pattern_ops);
 L   DROP INDEX public."multimedia_dulieudaphuongtien_maNhanDang_dcc76de2_like";
       public            postgres    false    327            R           1259    84639 -   multimedia_loaistyle_maNhanDang_3353ef9e_like    INDEX     �   CREATE INDEX "multimedia_loaistyle_maNhanDang_3353ef9e_like" ON public.multimedia_loaistyle USING btree ("maNhanDang" varchar_pattern_ops);
 C   DROP INDEX public."multimedia_loaistyle_maNhanDang_3353ef9e_like";
       public            postgres    false    322            W           1259    85591 -   multimedia_lopdulieu_maNhanDang_9c600cb7_like    INDEX     �   CREATE INDEX "multimedia_lopdulieu_maNhanDang_9c600cb7_like" ON public.multimedia_lopdulieu USING btree ("maNhanDang" varchar_pattern_ops);
 C   DROP INDEX public."multimedia_lopdulieu_maNhanDang_9c600cb7_like";
       public            postgres    false    323            X           1259    85581 '   multimedia_lopdulieu_maNhom_id_49e0da52    INDEX     q   CREATE INDEX "multimedia_lopdulieu_maNhom_id_49e0da52" ON public.multimedia_lopdulieu USING btree ("nhomDL_id");
 =   DROP INDEX public."multimedia_lopdulieu_maNhom_id_49e0da52";
       public            postgres    false    323            Y           1259    85582 ,   multimedia_lopdulieu_maNhom_id_49e0da52_like    INDEX     �   CREATE INDEX "multimedia_lopdulieu_maNhom_id_49e0da52_like" ON public.multimedia_lopdulieu USING btree ("nhomDL_id" varchar_pattern_ops);
 B   DROP INDEX public."multimedia_lopdulieu_maNhom_id_49e0da52_like";
       public            postgres    false    323            f           1259    85596 %   multimedia_metadata_maLop_id_85a23344    INDEX     m   CREATE INDEX "multimedia_metadata_maLop_id_85a23344" ON public.multimedia_metadata USING btree ("maLop_id");
 ;   DROP INDEX public."multimedia_metadata_maLop_id_85a23344";
       public            postgres    false    326            g           1259    85597 *   multimedia_metadata_maLop_id_85a23344_like    INDEX     �   CREATE INDEX "multimedia_metadata_maLop_id_85a23344_like" ON public.multimedia_metadata USING btree ("maLop_id" varchar_pattern_ops);
 @   DROP INDEX public."multimedia_metadata_maLop_id_85a23344_like";
       public            postgres    false    326            h           1259    84662 ,   multimedia_metadata_maNhanDang_fd89fa75_like    INDEX     �   CREATE INDEX "multimedia_metadata_maNhanDang_fd89fa75_like" ON public.multimedia_metadata USING btree ("maNhanDang" varchar_pattern_ops);
 B   DROP INDEX public."multimedia_metadata_maNhanDang_fd89fa75_like";
       public            postgres    false    326            \           1259    85580 .   multimedia_nhomdulieu_maNhanDang_bedd3360_like    INDEX     �   CREATE INDEX "multimedia_nhomdulieu_maNhanDang_bedd3360_like" ON public.multimedia_nhomdulieu USING btree ("maNhanDang" varchar_pattern_ops);
 D   DROP INDEX public."multimedia_nhomdulieu_maNhanDang_bedd3360_like";
       public            postgres    false    324            _           1259    84653 (   multimedia_style_maLoaiStyle_id_4a70fe18    INDEX     s   CREATE INDEX "multimedia_style_maLoaiStyle_id_4a70fe18" ON public.multimedia_style USING btree ("maLoaiStyle_id");
 >   DROP INDEX public."multimedia_style_maLoaiStyle_id_4a70fe18";
       public            postgres    false    325            `           1259    84654 -   multimedia_style_maLoaiStyle_id_4a70fe18_like    INDEX     �   CREATE INDEX "multimedia_style_maLoaiStyle_id_4a70fe18_like" ON public.multimedia_style USING btree ("maLoaiStyle_id" varchar_pattern_ops);
 C   DROP INDEX public."multimedia_style_maLoaiStyle_id_4a70fe18_like";
       public            postgres    false    325            a           1259    85592 "   multimedia_style_maLop_id_62c9d9bd    INDEX     g   CREATE INDEX "multimedia_style_maLop_id_62c9d9bd" ON public.multimedia_style USING btree ("maLop_id");
 8   DROP INDEX public."multimedia_style_maLop_id_62c9d9bd";
       public            postgres    false    325            b           1259    85593 '   multimedia_style_maLop_id_62c9d9bd_like    INDEX     �   CREATE INDEX "multimedia_style_maLop_id_62c9d9bd_like" ON public.multimedia_style USING btree ("maLop_id" varchar_pattern_ops);
 =   DROP INDEX public."multimedia_style_maLop_id_62c9d9bd_like";
       public            postgres    false    325            c           1259    84652 )   multimedia_style_maNhanDang_940983f2_like    INDEX     �   CREATE INDEX "multimedia_style_maNhanDang_940983f2_like" ON public.multimedia_style USING btree ("maNhanDang" varchar_pattern_ops);
 ?   DROP INDEX public."multimedia_style_maNhanDang_940983f2_like";
       public            postgres    false    325            p           1259    84732 %   phubemat_bematcongtrinh_GM_Surface_id    INDEX     r   CREATE INDEX "phubemat_bematcongtrinh_GM_Surface_id" ON public.phubemat_bematcongtrinh USING gist ("GM_Surface");
 ;   DROP INDEX public."phubemat_bematcongtrinh_GM_Surface_id";
       public            postgres    false    328    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2            q           1259    84731 0   phubemat_bematcongtrinh_maNhanDang_da90ef41_like    INDEX     �   CREATE INDEX "phubemat_bematcongtrinh_maNhanDang_da90ef41_like" ON public.phubemat_bematcongtrinh USING btree (manhandang varchar_pattern_ops);
 F   DROP INDEX public."phubemat_bematcongtrinh_maNhanDang_da90ef41_like";
       public            postgres    false    328            t           1259    84734 $   phubemat_bematkhudancu_GM_Surface_id    INDEX     p   CREATE INDEX "phubemat_bematkhudancu_GM_Surface_id" ON public.phubemat_bematkhudancu USING gist ("GM_Surface");
 :   DROP INDEX public."phubemat_bematkhudancu_GM_Surface_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    329            u           1259    84733 /   phubemat_bematkhudancu_maNhanDang_024e293f_like    INDEX     �   CREATE INDEX "phubemat_bematkhudancu_maNhanDang_024e293f_like" ON public.phubemat_bematkhudancu USING btree (manhandang varchar_pattern_ops);
 E   DROP INDEX public."phubemat_bematkhudancu_maNhanDang_024e293f_like";
       public            postgres    false    329            x           1259    84736    phubemat_caydoclap_GM_Point_id    INDEX     d   CREATE INDEX "phubemat_caydoclap_GM_Point_id" ON public.phubemat_caydoclap USING gist ("GM_Point");
 4   DROP INDEX public."phubemat_caydoclap_GM_Point_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    330            y           1259    84735 +   phubemat_caydoclap_maNhanDang_92fb887f_like    INDEX     �   CREATE INDEX "phubemat_caydoclap_maNhanDang_92fb887f_like" ON public.phubemat_caydoclap USING btree (manhandang varchar_pattern_ops);
 A   DROP INDEX public."phubemat_caydoclap_maNhanDang_92fb887f_like";
       public            postgres    false    330            |           1259    84738    phubemat_dattrong_GM_Surface_id    INDEX     f   CREATE INDEX "phubemat_dattrong_GM_Surface_id" ON public.phubemat_dattrong USING gist ("GM_Surface");
 5   DROP INDEX public."phubemat_dattrong_GM_Surface_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    331            }           1259    84737 *   phubemat_dattrong_maNhanDang_14ac0187_like    INDEX     �   CREATE INDEX "phubemat_dattrong_maNhanDang_14ac0187_like" ON public.phubemat_dattrong USING btree (manhandang varchar_pattern_ops);
 @   DROP INDEX public."phubemat_dattrong_maNhanDang_14ac0187_like";
       public            postgres    false    331            �           1259    84740    phubemat_nuocmat_GM_Surface_id    INDEX     d   CREATE INDEX "phubemat_nuocmat_GM_Surface_id" ON public.phubemat_nuocmat USING gist ("GM_Surface");
 4   DROP INDEX public."phubemat_nuocmat_GM_Surface_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    332            �           1259    84739 )   phubemat_nuocmat_maNhanDang_dc2155ad_like    INDEX     �   CREATE INDEX "phubemat_nuocmat_maNhanDang_dc2155ad_like" ON public.phubemat_nuocmat USING btree (manhandang varchar_pattern_ops);
 ?   DROP INDEX public."phubemat_nuocmat_maNhanDang_dc2155ad_like";
       public            postgres    false    332            �           1259    84742 %   phubemat_ranhgioiphubemat_GM_Curve_id    INDEX     r   CREATE INDEX "phubemat_ranhgioiphubemat_GM_Curve_id" ON public.phubemat_ranhgioiphubemat USING gist ("GM_Curve");
 ;   DROP INDEX public."phubemat_ranhgioiphubemat_GM_Curve_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    333            �           1259    84741 2   phubemat_ranhgioiphubemat_maNhanDang_7ee9d9df_like    INDEX     �   CREATE INDEX "phubemat_ranhgioiphubemat_maNhanDang_7ee9d9df_like" ON public.phubemat_ranhgioiphubemat USING btree (manhandang varchar_pattern_ops);
 H   DROP INDEX public."phubemat_ranhgioiphubemat_maNhanDang_7ee9d9df_like";
       public            postgres    false    333            �           1259    84744 %   phubemat_thucvatdaybien_GM_Surface_id    INDEX     r   CREATE INDEX "phubemat_thucvatdaybien_GM_Surface_id" ON public.phubemat_thucvatdaybien USING gist ("GM_Surface");
 ;   DROP INDEX public."phubemat_thucvatdaybien_GM_Surface_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    334            �           1259    84743 0   phubemat_thucvatdaybien_maNhanDang_59013f53_like    INDEX     �   CREATE INDEX "phubemat_thucvatdaybien_maNhanDang_59013f53_like" ON public.phubemat_thucvatdaybien USING btree (manhandang varchar_pattern_ops);
 F   DROP INDEX public."phubemat_thucvatdaybien_maNhanDang_59013f53_like";
       public            postgres    false    334            �           1259    84999 #   soanthaokehoach_diemnvdh_geoDiem_id    INDEX     n   CREATE INDEX "soanthaokehoach_diemnvdh_geoDiem_id" ON public.soanthaokehoach_diemnvdh USING gist ("geoDiem");
 9   DROP INDEX public."soanthaokehoach_diemnvdh_geoDiem_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    349            �           1259    84998 1   soanthaokehoach_diemnvdh_maNhanDang_0c88e341_like    INDEX     �   CREATE INDEX "soanthaokehoach_diemnvdh_maNhanDang_0c88e341_like" ON public.soanthaokehoach_diemnvdh USING btree ("maNhanDang" varchar_pattern_ops);
 G   DROP INDEX public."soanthaokehoach_diemnvdh_maNhanDang_0c88e341_like";
       public            postgres    false    349            �           1259    85000 )   soanthaokehoach_diemnvdh_nvdh_id_0036ead6    INDEX     q   CREATE INDEX soanthaokehoach_diemnvdh_nvdh_id_0036ead6 ON public.soanthaokehoach_diemnvdh USING btree (nvdh_id);
 =   DROP INDEX public.soanthaokehoach_diemnvdh_nvdh_id_0036ead6;
       public            postgres    false    349            �           1259    85001 .   soanthaokehoach_diemnvdh_nvdh_id_0036ead6_like    INDEX     �   CREATE INDEX soanthaokehoach_diemnvdh_nvdh_id_0036ead6_like ON public.soanthaokehoach_diemnvdh USING btree (nvdh_id varchar_pattern_ops);
 B   DROP INDEX public.soanthaokehoach_diemnvdh_nvdh_id_0036ead6_like;
       public            postgres    false    349            �           1259    84887 4   soanthaokehoach_ganlucluong_maNhanDang_15f98967_like    INDEX     �   CREATE INDEX "soanthaokehoach_ganlucluong_maNhanDang_15f98967_like" ON public.soanthaokehoach_ganlucluong USING btree ("maNhanDang" varchar_pattern_ops);
 J   DROP INDEX public."soanthaokehoach_ganlucluong_maNhanDang_15f98967_like";
       public            postgres    false    336            �           1259    84987 +   soanthaokehoach_ganlucluong_pat_id_c136a398    INDEX     u   CREATE INDEX soanthaokehoach_ganlucluong_pat_id_c136a398 ON public.soanthaokehoach_ganlucluong USING btree (pat_id);
 ?   DROP INDEX public.soanthaokehoach_ganlucluong_pat_id_c136a398;
       public            postgres    false    336            �           1259    84988 0   soanthaokehoach_ganlucluong_pat_id_c136a398_like    INDEX     �   CREATE INDEX soanthaokehoach_ganlucluong_pat_id_c136a398_like ON public.soanthaokehoach_ganlucluong USING btree (pat_id varchar_pattern_ops);
 D   DROP INDEX public.soanthaokehoach_ganlucluong_pat_id_c136a398_like;
       public            postgres    false    336            �           1259    84989 +   soanthaokehoach_ganlucluong_pav_id_5589b6c1    INDEX     u   CREATE INDEX soanthaokehoach_ganlucluong_pav_id_5589b6c1 ON public.soanthaokehoach_ganlucluong USING btree (pav_id);
 ?   DROP INDEX public.soanthaokehoach_ganlucluong_pav_id_5589b6c1;
       public            postgres    false    336            �           1259    84990 0   soanthaokehoach_ganlucluong_pav_id_5589b6c1_like    INDEX     �   CREATE INDEX soanthaokehoach_ganlucluong_pav_id_5589b6c1_like ON public.soanthaokehoach_ganlucluong USING btree (pav_id varchar_pattern_ops);
 D   DROP INDEX public.soanthaokehoach_ganlucluong_pav_id_5589b6c1_like;
       public            postgres    false    336            �           1259    84991 ,   soanthaokehoach_ganlucluong_pavt_id_704f22bd    INDEX     w   CREATE INDEX soanthaokehoach_ganlucluong_pavt_id_704f22bd ON public.soanthaokehoach_ganlucluong USING btree (pavt_id);
 @   DROP INDEX public.soanthaokehoach_ganlucluong_pavt_id_704f22bd;
       public            postgres    false    336            �           1259    84992 1   soanthaokehoach_ganlucluong_pavt_id_704f22bd_like    INDEX     �   CREATE INDEX soanthaokehoach_ganlucluong_pavt_id_704f22bd_like ON public.soanthaokehoach_ganlucluong USING btree (pavt_id varchar_pattern_ops);
 E   DROP INDEX public.soanthaokehoach_ganlucluong_pavt_id_704f22bd_like;
       public            postgres    false    336            �           1259    84894 %   soanthaokehoach_nvbp_maDV_id_87b2c8ac    INDEX     m   CREATE INDEX "soanthaokehoach_nvbp_maDV_id_87b2c8ac" ON public.soanthaokehoach_nvbp USING btree ("maDV_id");
 ;   DROP INDEX public."soanthaokehoach_nvbp_maDV_id_87b2c8ac";
       public            postgres    false    337            �           1259    84895 *   soanthaokehoach_nvbp_maDV_id_87b2c8ac_like    INDEX     �   CREATE INDEX "soanthaokehoach_nvbp_maDV_id_87b2c8ac_like" ON public.soanthaokehoach_nvbp USING btree ("maDV_id" varchar_pattern_ops);
 @   DROP INDEX public."soanthaokehoach_nvbp_maDV_id_87b2c8ac_like";
       public            postgres    false    337            �           1259    84985 '   soanthaokehoach_nvbp_maNVDH_id_9bf11f77    INDEX     q   CREATE INDEX "soanthaokehoach_nvbp_maNVDH_id_9bf11f77" ON public.soanthaokehoach_nvbp USING btree ("maNVDH_id");
 =   DROP INDEX public."soanthaokehoach_nvbp_maNVDH_id_9bf11f77";
       public            postgres    false    337            �           1259    84986 ,   soanthaokehoach_nvbp_maNVDH_id_9bf11f77_like    INDEX     �   CREATE INDEX "soanthaokehoach_nvbp_maNVDH_id_9bf11f77_like" ON public.soanthaokehoach_nvbp USING btree ("maNVDH_id" varchar_pattern_ops);
 B   DROP INDEX public."soanthaokehoach_nvbp_maNVDH_id_9bf11f77_like";
       public            postgres    false    337            �           1259    84893 -   soanthaokehoach_nvbp_maNhanDang_b923f14e_like    INDEX     �   CREATE INDEX "soanthaokehoach_nvbp_maNhanDang_b923f14e_like" ON public.soanthaokehoach_nvbp USING btree ("maNhanDang" varchar_pattern_ops);
 C   DROP INDEX public."soanthaokehoach_nvbp_maNhanDang_b923f14e_like";
       public            postgres    false    337            �           1259    84896 -   soanthaokehoach_nvdh_maNhanDang_19835851_like    INDEX     �   CREATE INDEX "soanthaokehoach_nvdh_maNhanDang_19835851_like" ON public.soanthaokehoach_nvdh USING btree ("maNhanDang" varchar_pattern_ops);
 C   DROP INDEX public."soanthaokehoach_nvdh_maNhanDang_19835851_like";
       public            postgres    false    338            �           1259    84976 /   soanthaokehoach_pheduyet_ganLL_id_c3cec84e_like    INDEX     �   CREATE INDEX "soanthaokehoach_pheduyet_ganLL_id_c3cec84e_like" ON public.soanthaokehoach_pheduyetphuonganganlucluong USING btree ("ganLL_id" varchar_pattern_ops);
 E   DROP INDEX public."soanthaokehoach_pheduyet_ganLL_id_c3cec84e_like";
       public            postgres    false    347            �           1259    84974 1   soanthaokehoach_pheduyet_maNhanDang_daefbe99_like    INDEX     �   CREATE INDEX "soanthaokehoach_pheduyet_maNhanDang_daefbe99_like" ON public.soanthaokehoach_pheduyetphuonganganlucluong USING btree ("maNhanDang" varchar_pattern_ops);
 G   DROP INDEX public."soanthaokehoach_pheduyet_maNhanDang_daefbe99_like";
       public            postgres    false    347            �           1259    84982 :   soanthaokehoach_pheduyetchungnvbp_maNhanDang_b2a193d7_like    INDEX     �   CREATE INDEX "soanthaokehoach_pheduyetchungnvbp_maNhanDang_b2a193d7_like" ON public.soanthaokehoach_pheduyetchungnvbp USING btree ("maNhanDang" varchar_pattern_ops);
 P   DROP INDEX public."soanthaokehoach_pheduyetchungnvbp_maNhanDang_b2a193d7_like";
       public            postgres    false    348            �           1259    84983 2   soanthaokehoach_pheduyetchungnvbp_nvbp_id_d82658f9    INDEX     �   CREATE INDEX soanthaokehoach_pheduyetchungnvbp_nvbp_id_d82658f9 ON public.soanthaokehoach_pheduyetchungnvbp USING btree (nvbp_id);
 F   DROP INDEX public.soanthaokehoach_pheduyetchungnvbp_nvbp_id_d82658f9;
       public            postgres    false    348            �           1259    84984 7   soanthaokehoach_pheduyetchungnvbp_nvbp_id_d82658f9_like    INDEX     �   CREATE INDEX soanthaokehoach_pheduyetchungnvbp_nvbp_id_d82658f9_like ON public.soanthaokehoach_pheduyetchungnvbp USING btree (nvbp_id varchar_pattern_ops);
 K   DROP INDEX public.soanthaokehoach_pheduyetchungnvbp_nvbp_id_d82658f9_like;
       public            postgres    false    348            �           1259    84975 =   soanthaokehoach_pheduyetphuonganganlucluong_ganLL_id_c3cec84e    INDEX     �   CREATE INDEX "soanthaokehoach_pheduyetphuonganganlucluong_ganLL_id_c3cec84e" ON public.soanthaokehoach_pheduyetphuonganganlucluong USING btree ("ganLL_id");
 S   DROP INDEX public."soanthaokehoach_pheduyetphuonganganlucluong_ganLL_id_c3cec84e";
       public            postgres    false    347            �           1259    84966 5   soanthaokehoach_pheduyetphuongantuyen_geoCMPATuyen_id    INDEX     �   CREATE INDEX "soanthaokehoach_pheduyetphuongantuyen_geoCMPATuyen_id" ON public.soanthaokehoach_pheduyetphuongantuyen USING gist ("geoCMPATuyen");
 K   DROP INDEX public."soanthaokehoach_pheduyetphuongantuyen_geoCMPATuyen_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    346            �           1259    84965 >   soanthaokehoach_pheduyetphuongantuyen_maNhanDang_b3503ada_like    INDEX     �   CREATE INDEX "soanthaokehoach_pheduyetphuongantuyen_maNhanDang_b3503ada_like" ON public.soanthaokehoach_pheduyetphuongantuyen USING btree ("maNhanDang" varchar_pattern_ops);
 T   DROP INDEX public."soanthaokehoach_pheduyetphuongantuyen_maNhanDang_b3503ada_like";
       public            postgres    false    346            �           1259    84967 9   soanthaokehoach_pheduyetphuongantuyen_paTuyen_id_cea8cdf2    INDEX     �   CREATE INDEX "soanthaokehoach_pheduyetphuongantuyen_paTuyen_id_cea8cdf2" ON public.soanthaokehoach_pheduyetphuongantuyen USING btree ("paTuyen_id");
 O   DROP INDEX public."soanthaokehoach_pheduyetphuongantuyen_paTuyen_id_cea8cdf2";
       public            postgres    false    346            �           1259    84968 >   soanthaokehoach_pheduyetphuongantuyen_paTuyen_id_cea8cdf2_like    INDEX     �   CREATE INDEX "soanthaokehoach_pheduyetphuongantuyen_paTuyen_id_cea8cdf2_like" ON public.soanthaokehoach_pheduyetphuongantuyen USING btree ("paTuyen_id" varchar_pattern_ops);
 T   DROP INDEX public."soanthaokehoach_pheduyetphuongantuyen_paTuyen_id_cea8cdf2_like";
       public            postgres    false    346            �           1259    84957 2   soanthaokehoach_pheduyetphuonganvitri_geoCMPAVT_id    INDEX     �   CREATE INDEX "soanthaokehoach_pheduyetphuonganvitri_geoCMPAVT_id" ON public.soanthaokehoach_pheduyetphuonganvitri USING gist ("geoCMPAVT");
 H   DROP INDEX public."soanthaokehoach_pheduyetphuonganvitri_geoCMPAVT_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    345            �           1259    84956 >   soanthaokehoach_pheduyetphuonganvitri_maNhanDang_4f513be8_like    INDEX     �   CREATE INDEX "soanthaokehoach_pheduyetphuonganvitri_maNhanDang_4f513be8_like" ON public.soanthaokehoach_pheduyetphuonganvitri USING btree ("maNhanDang" varchar_pattern_ops);
 T   DROP INDEX public."soanthaokehoach_pheduyetphuonganvitri_maNhanDang_4f513be8_like";
       public            postgres    false    345            �           1259    84958 9   soanthaokehoach_pheduyetphuonganvitri_paViTri_id_996e5b8f    INDEX     �   CREATE INDEX "soanthaokehoach_pheduyetphuonganvitri_paViTri_id_996e5b8f" ON public.soanthaokehoach_pheduyetphuonganvitri USING btree ("paViTri_id");
 O   DROP INDEX public."soanthaokehoach_pheduyetphuonganvitri_paViTri_id_996e5b8f";
       public            postgres    false    345            �           1259    84959 >   soanthaokehoach_pheduyetphuonganvitri_paViTri_id_996e5b8f_like    INDEX     �   CREATE INDEX "soanthaokehoach_pheduyetphuonganvitri_paViTri_id_996e5b8f_like" ON public.soanthaokehoach_pheduyetphuonganvitri USING btree ("paViTri_id" varchar_pattern_ops);
 T   DROP INDEX public."soanthaokehoach_pheduyetphuonganvitri_paViTri_id_996e5b8f_like";
       public            postgres    false    345            �           1259    84948 3   soanthaokehoach_pheduyetphuonganvung_geoCMPAVung_id    INDEX     �   CREATE INDEX "soanthaokehoach_pheduyetphuonganvung_geoCMPAVung_id" ON public.soanthaokehoach_pheduyetphuonganvung USING gist ("geoCMPAVung");
 I   DROP INDEX public."soanthaokehoach_pheduyetphuonganvung_geoCMPAVung_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    344            �           1259    84947 =   soanthaokehoach_pheduyetphuonganvung_maNhanDang_6c241a74_like    INDEX     �   CREATE INDEX "soanthaokehoach_pheduyetphuonganvung_maNhanDang_6c241a74_like" ON public.soanthaokehoach_pheduyetphuonganvung USING btree ("maNhanDang" varchar_pattern_ops);
 S   DROP INDEX public."soanthaokehoach_pheduyetphuonganvung_maNhanDang_6c241a74_like";
       public            postgres    false    344            �           1259    84949 7   soanthaokehoach_pheduyetphuonganvung_paVung_id_07d3ee65    INDEX     �   CREATE INDEX "soanthaokehoach_pheduyetphuonganvung_paVung_id_07d3ee65" ON public.soanthaokehoach_pheduyetphuonganvung USING btree ("paVung_id");
 M   DROP INDEX public."soanthaokehoach_pheduyetphuonganvung_paVung_id_07d3ee65";
       public            postgres    false    344            �           1259    84950 <   soanthaokehoach_pheduyetphuonganvung_paVung_id_07d3ee65_like    INDEX     �   CREATE INDEX "soanthaokehoach_pheduyetphuonganvung_paVung_id_07d3ee65_like" ON public.soanthaokehoach_pheduyetphuonganvung USING btree ("paVung_id" varchar_pattern_ops);
 R   DROP INDEX public."soanthaokehoach_pheduyetphuonganvung_paVung_id_07d3ee65_like";
       public            postgres    false    344            �           1259    84939 +   soanthaokehoach_phuongantuyen_geoPATuyen_id    INDEX     ~   CREATE INDEX "soanthaokehoach_phuongantuyen_geoPATuyen_id" ON public.soanthaokehoach_phuongantuyen USING gist ("geoPATuyen");
 A   DROP INDEX public."soanthaokehoach_phuongantuyen_geoPATuyen_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    343            �           1259    84938 6   soanthaokehoach_phuongantuyen_maNhanDang_c70f6c1a_like    INDEX     �   CREATE INDEX "soanthaokehoach_phuongantuyen_maNhanDang_c70f6c1a_like" ON public.soanthaokehoach_phuongantuyen USING btree ("maNhanDang" varchar_pattern_ops);
 L   DROP INDEX public."soanthaokehoach_phuongantuyen_maNhanDang_c70f6c1a_like";
       public            postgres    false    343            �           1259    84940 .   soanthaokehoach_phuongantuyen_nvbp_id_133e3389    INDEX     {   CREATE INDEX soanthaokehoach_phuongantuyen_nvbp_id_133e3389 ON public.soanthaokehoach_phuongantuyen USING btree (nvbp_id);
 B   DROP INDEX public.soanthaokehoach_phuongantuyen_nvbp_id_133e3389;
       public            postgres    false    343            �           1259    84941 3   soanthaokehoach_phuongantuyen_nvbp_id_133e3389_like    INDEX     �   CREATE INDEX soanthaokehoach_phuongantuyen_nvbp_id_133e3389_like ON public.soanthaokehoach_phuongantuyen USING btree (nvbp_id varchar_pattern_ops);
 G   DROP INDEX public.soanthaokehoach_phuongantuyen_nvbp_id_133e3389_like;
       public            postgres    false    343            �           1259    84930 (   soanthaokehoach_phuonganvitri_geoPAVT_id    INDEX     x   CREATE INDEX "soanthaokehoach_phuonganvitri_geoPAVT_id" ON public.soanthaokehoach_phuonganvitri USING gist ("geoPAVT");
 >   DROP INDEX public."soanthaokehoach_phuonganvitri_geoPAVT_id";
       public            postgres    false    342    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2            �           1259    84929 6   soanthaokehoach_phuonganvitri_maNhanDang_59d57a95_like    INDEX     �   CREATE INDEX "soanthaokehoach_phuonganvitri_maNhanDang_59d57a95_like" ON public.soanthaokehoach_phuonganvitri USING btree ("maNhanDang" varchar_pattern_ops);
 L   DROP INDEX public."soanthaokehoach_phuonganvitri_maNhanDang_59d57a95_like";
       public            postgres    false    342            �           1259    84931 .   soanthaokehoach_phuonganvitri_nvbp_id_c1e6acb3    INDEX     {   CREATE INDEX soanthaokehoach_phuonganvitri_nvbp_id_c1e6acb3 ON public.soanthaokehoach_phuonganvitri USING btree (nvbp_id);
 B   DROP INDEX public.soanthaokehoach_phuonganvitri_nvbp_id_c1e6acb3;
       public            postgres    false    342            �           1259    84932 3   soanthaokehoach_phuonganvitri_nvbp_id_c1e6acb3_like    INDEX     �   CREATE INDEX soanthaokehoach_phuonganvitri_nvbp_id_c1e6acb3_like ON public.soanthaokehoach_phuonganvitri USING btree (nvbp_id varchar_pattern_ops);
 G   DROP INDEX public.soanthaokehoach_phuonganvitri_nvbp_id_c1e6acb3_like;
       public            postgres    false    342            �           1259    84921 )   soanthaokehoach_phuonganvung_geoPAVung_id    INDEX     z   CREATE INDEX "soanthaokehoach_phuonganvung_geoPAVung_id" ON public.soanthaokehoach_phuonganvung USING gist ("geoPAVung");
 ?   DROP INDEX public."soanthaokehoach_phuonganvung_geoPAVung_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    341            �           1259    84920 5   soanthaokehoach_phuonganvung_maNhanDang_cb800df5_like    INDEX     �   CREATE INDEX "soanthaokehoach_phuonganvung_maNhanDang_cb800df5_like" ON public.soanthaokehoach_phuonganvung USING btree ("maNhanDang" varchar_pattern_ops);
 K   DROP INDEX public."soanthaokehoach_phuonganvung_maNhanDang_cb800df5_like";
       public            postgres    false    341            �           1259    84922 -   soanthaokehoach_phuonganvung_nvbp_id_a105a16e    INDEX     y   CREATE INDEX soanthaokehoach_phuonganvung_nvbp_id_a105a16e ON public.soanthaokehoach_phuonganvung USING btree (nvbp_id);
 A   DROP INDEX public.soanthaokehoach_phuonganvung_nvbp_id_a105a16e;
       public            postgres    false    341            �           1259    84923 2   soanthaokehoach_phuonganvung_nvbp_id_a105a16e_like    INDEX     �   CREATE INDEX soanthaokehoach_phuonganvung_nvbp_id_a105a16e_like ON public.soanthaokehoach_phuonganvung USING btree (nvbp_id varchar_pattern_ops);
 F   DROP INDEX public.soanthaokehoach_phuonganvung_nvbp_id_a105a16e_like;
       public            postgres    false    341            �           1259    84912 %   soanthaokehoach_tuyennvdh_geoTuyen_id    INDEX     r   CREATE INDEX "soanthaokehoach_tuyennvdh_geoTuyen_id" ON public.soanthaokehoach_tuyennvdh USING gist ("geoTuyen");
 ;   DROP INDEX public."soanthaokehoach_tuyennvdh_geoTuyen_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    340            �           1259    84911 2   soanthaokehoach_tuyennvdh_maNhanDang_aafe0b1b_like    INDEX     �   CREATE INDEX "soanthaokehoach_tuyennvdh_maNhanDang_aafe0b1b_like" ON public.soanthaokehoach_tuyennvdh USING btree ("maNhanDang" varchar_pattern_ops);
 H   DROP INDEX public."soanthaokehoach_tuyennvdh_maNhanDang_aafe0b1b_like";
       public            postgres    false    340            �           1259    84913 *   soanthaokehoach_tuyennvdh_nvdh_id_094789c0    INDEX     s   CREATE INDEX soanthaokehoach_tuyennvdh_nvdh_id_094789c0 ON public.soanthaokehoach_tuyennvdh USING btree (nvdh_id);
 >   DROP INDEX public.soanthaokehoach_tuyennvdh_nvdh_id_094789c0;
       public            postgres    false    340            �           1259    84914 /   soanthaokehoach_tuyennvdh_nvdh_id_094789c0_like    INDEX     �   CREATE INDEX soanthaokehoach_tuyennvdh_nvdh_id_094789c0_like ON public.soanthaokehoach_tuyennvdh USING btree (nvdh_id varchar_pattern_ops);
 C   DROP INDEX public.soanthaokehoach_tuyennvdh_nvdh_id_094789c0_like;
       public            postgres    false    340            �           1259    84903 #   soanthaokehoach_vungnvdh_geoVung_id    INDEX     n   CREATE INDEX "soanthaokehoach_vungnvdh_geoVung_id" ON public.soanthaokehoach_vungnvdh USING gist ("geoVung");
 9   DROP INDEX public."soanthaokehoach_vungnvdh_geoVung_id";
       public            postgres    false    339    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2            �           1259    84902 1   soanthaokehoach_vungnvdh_maNhanDang_3e0b2e65_like    INDEX     �   CREATE INDEX "soanthaokehoach_vungnvdh_maNhanDang_3e0b2e65_like" ON public.soanthaokehoach_vungnvdh USING btree ("maNhanDang" varchar_pattern_ops);
 G   DROP INDEX public."soanthaokehoach_vungnvdh_maNhanDang_3e0b2e65_like";
       public            postgres    false    339            �           1259    84904 )   soanthaokehoach_vungnvdh_nvdh_id_cc249707    INDEX     q   CREATE INDEX soanthaokehoach_vungnvdh_nvdh_id_cc249707 ON public.soanthaokehoach_vungnvdh USING btree (nvdh_id);
 =   DROP INDEX public.soanthaokehoach_vungnvdh_nvdh_id_cc249707;
       public            postgres    false    339            �           1259    84905 .   soanthaokehoach_vungnvdh_nvdh_id_cc249707_like    INDEX     �   CREATE INDEX soanthaokehoach_vungnvdh_nvdh_id_cc249707_like ON public.soanthaokehoach_vungnvdh USING btree (nvdh_id varchar_pattern_ops);
 B   DROP INDEX public.soanthaokehoach_vungnvdh_nvdh_id_cc249707_like;
       public            postgres    false    339            D           1259    85646    test_mymodel_choice_id_14e4a959    INDEX     ]   CREATE INDEX test_mymodel_choice_id_14e4a959 ON public.test_mymodel USING btree (choice_id);
 3   DROP INDEX public.test_mymodel_choice_id_14e4a959;
       public            postgres    false    379            E           1259    85645    test_mymodel_id_fe791470_like    INDEX     h   CREATE INDEX test_mymodel_id_fe791470_like ON public.test_mymodel USING btree (id varchar_pattern_ops);
 1   DROP INDEX public.test_mymodel_id_fe791470_like;
       public            postgres    false    379            �           1259    85174    thuyvan_bokebocap_GM_Curve_id    INDEX     b   CREATE INDEX "thuyvan_bokebocap_GM_Curve_id" ON public.thuyvan_bokebocap USING gist ("GM_Curve");
 3   DROP INDEX public."thuyvan_bokebocap_GM_Curve_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    350            �           1259    85173 *   thuyvan_bokebocap_maNhanDang_81c65d89_like    INDEX     �   CREATE INDEX "thuyvan_bokebocap_maNhanDang_81c65d89_like" ON public.thuyvan_bokebocap USING btree (manhandang varchar_pattern_ops);
 @   DROP INDEX public."thuyvan_bokebocap_maNhanDang_81c65d89_like";
       public            postgres    false    350            �           1259    85176 #   thuyvan_curve_kenhmuong_GM_Curve_id    INDEX     n   CREATE INDEX "thuyvan_curve_kenhmuong_GM_Curve_id" ON public.thuyvan_curve_kenhmuong USING gist ("GM_Curve");
 9   DROP INDEX public."thuyvan_curve_kenhmuong_GM_Curve_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    351            �           1259    85175 0   thuyvan_curve_kenhmuong_maNhanDang_5ee135da_like    INDEX     �   CREATE INDEX "thuyvan_curve_kenhmuong_maNhanDang_5ee135da_like" ON public.thuyvan_curve_kenhmuong USING btree (manhandang varchar_pattern_ops);
 F   DROP INDEX public."thuyvan_curve_kenhmuong_maNhanDang_5ee135da_like";
       public            postgres    false    351            �           1259    85178 $   thuyvan_diemdocaomucnuoc_GM_Point_id    INDEX     p   CREATE INDEX "thuyvan_diemdocaomucnuoc_GM_Point_id" ON public.thuyvan_diemdocaomucnuoc USING gist ("GM_Point");
 :   DROP INDEX public."thuyvan_diemdocaomucnuoc_GM_Point_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    352            �           1259    85177 1   thuyvan_diemdocaomucnuoc_maNhanDang_8b2af9f7_like    INDEX     �   CREATE INDEX "thuyvan_diemdocaomucnuoc_maNhanDang_8b2af9f7_like" ON public.thuyvan_diemdocaomucnuoc USING btree (manhandang varchar_pattern_ops);
 G   DROP INDEX public."thuyvan_diemdocaomucnuoc_maNhanDang_8b2af9f7_like";
       public            postgres    false    352            �           1259    85180    thuyvan_duongbonuoc_GM_Curve_id    INDEX     f   CREATE INDEX "thuyvan_duongbonuoc_GM_Curve_id" ON public.thuyvan_duongbonuoc USING gist ("GM_Curve");
 5   DROP INDEX public."thuyvan_duongbonuoc_GM_Curve_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    353            �           1259    85179 ,   thuyvan_duongbonuoc_maNhanDang_a413d34c_like    INDEX     �   CREATE INDEX "thuyvan_duongbonuoc_maNhanDang_a413d34c_like" ON public.thuyvan_duongbonuoc USING btree (manhandang varchar_pattern_ops);
 B   DROP INDEX public."thuyvan_duongbonuoc_maNhanDang_a413d34c_like";
       public            postgres    false    353            �           1259    85182     thuyvan_duongmepnuoc_GM_Curve_id    INDEX     h   CREATE INDEX "thuyvan_duongmepnuoc_GM_Curve_id" ON public.thuyvan_duongmepnuoc USING gist ("GM_Curve");
 6   DROP INDEX public."thuyvan_duongmepnuoc_GM_Curve_id";
       public            postgres    false    354    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2            �           1259    85181 -   thuyvan_duongmepnuoc_maNhanDang_1be160ab_like    INDEX     �   CREATE INDEX "thuyvan_duongmepnuoc_maNhanDang_1be160ab_like" ON public.thuyvan_duongmepnuoc USING btree (manhandang varchar_pattern_ops);
 C   DROP INDEX public."thuyvan_duongmepnuoc_maNhanDang_1be160ab_like";
       public            postgres    false    354            �           1259    85184     thuyvan_point_baiboi_GM_Point_id    INDEX     h   CREATE INDEX "thuyvan_point_baiboi_GM_Point_id" ON public.thuyvan_point_baiboi USING gist ("GM_Point");
 6   DROP INDEX public."thuyvan_point_baiboi_GM_Point_id";
       public            postgres    false    355    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2            �           1259    85183 -   thuyvan_point_baiboi_maNhanDang_50f042c5_like    INDEX     �   CREATE INDEX "thuyvan_point_baiboi_maNhanDang_50f042c5_like" ON public.thuyvan_point_baiboi USING btree (manhandang varchar_pattern_ops);
 C   DROP INDEX public."thuyvan_point_baiboi_maNhanDang_50f042c5_like";
       public            postgres    false    355            �           1259    85186 '   thuyvan_point_baidaduoinuoc_GM_Point_id    INDEX     v   CREATE INDEX "thuyvan_point_baidaduoinuoc_GM_Point_id" ON public.thuyvan_point_baidaduoinuoc USING gist ("GM_Point");
 =   DROP INDEX public."thuyvan_point_baidaduoinuoc_GM_Point_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    356            �           1259    85185 4   thuyvan_point_baidaduoinuoc_maNhanDang_a80bda73_like    INDEX     �   CREATE INDEX "thuyvan_point_baidaduoinuoc_maNhanDang_a80bda73_like" ON public.thuyvan_point_baidaduoinuoc USING btree (manhandang varchar_pattern_ops);
 J   DROP INDEX public."thuyvan_point_baidaduoinuoc_maNhanDang_a80bda73_like";
       public            postgres    false    356            �           1259    85188 !   thuyvan_point_biendao_GM_Point_id    INDEX     j   CREATE INDEX "thuyvan_point_biendao_GM_Point_id" ON public.thuyvan_point_biendao USING gist ("GM_Point");
 7   DROP INDEX public."thuyvan_point_biendao_GM_Point_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    357                        1259    85187 .   thuyvan_point_biendao_maNhanDang_5de05d4b_like    INDEX     �   CREATE INDEX "thuyvan_point_biendao_maNhanDang_5de05d4b_like" ON public.thuyvan_point_biendao USING btree (manhandang varchar_pattern_ops);
 D   DROP INDEX public."thuyvan_point_biendao_maNhanDang_5de05d4b_like";
       public            postgres    false    357                       1259    85190    thuyvan_point_dao_GM_Point_id    INDEX     b   CREATE INDEX "thuyvan_point_dao_GM_Point_id" ON public.thuyvan_point_dao USING gist ("GM_Point");
 3   DROP INDEX public."thuyvan_point_dao_GM_Point_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    358                       1259    85189 *   thuyvan_point_dao_maNhanDang_20c4991b_like    INDEX     �   CREATE INDEX "thuyvan_point_dao_maNhanDang_20c4991b_like" ON public.thuyvan_point_dao USING btree (manhandang varchar_pattern_ops);
 @   DROP INDEX public."thuyvan_point_dao_maNhanDang_20c4991b_like";
       public            postgres    false    358                       1259    85192 #   thuyvan_point_nguonnuoc_GM_Point_id    INDEX     n   CREATE INDEX "thuyvan_point_nguonnuoc_GM_Point_id" ON public.thuyvan_point_nguonnuoc USING gist ("GM_Point");
 9   DROP INDEX public."thuyvan_point_nguonnuoc_GM_Point_id";
       public            postgres    false    359    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2                       1259    85191 0   thuyvan_point_nguonnuoc_maNhanDang_17721eb5_like    INDEX     �   CREATE INDEX "thuyvan_point_nguonnuoc_maNhanDang_17721eb5_like" ON public.thuyvan_point_nguonnuoc USING btree (manhandang varchar_pattern_ops);
 F   DROP INDEX public."thuyvan_point_nguonnuoc_maNhanDang_17721eb5_like";
       public            postgres    false    359                       1259    85194 )   thuyvan_ranhgioinuocmatquyuoc_GM_Curve_id    INDEX     z   CREATE INDEX "thuyvan_ranhgioinuocmatquyuoc_GM_Curve_id" ON public.thuyvan_ranhgioinuocmatquyuoc USING gist ("GM_Curve");
 ?   DROP INDEX public."thuyvan_ranhgioinuocmatquyuoc_GM_Curve_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    360                       1259    85193 6   thuyvan_ranhgioinuocmatquyuoc_maNhanDang_92445ab8_like    INDEX     �   CREATE INDEX "thuyvan_ranhgioinuocmatquyuoc_maNhanDang_92445ab8_like" ON public.thuyvan_ranhgioinuocmatquyuoc USING btree (manhandang varchar_pattern_ops);
 L   DROP INDEX public."thuyvan_ranhgioinuocmatquyuoc_maNhanDang_92445ab8_like";
       public            postgres    false    360            5           1259    85228 ,   thuyvan_songgiodongchay_tramKTTV_id_5bdc07d2    INDEX     {   CREATE INDEX "thuyvan_songgiodongchay_tramKTTV_id_5bdc07d2" ON public.thuyvan_songgiodongchay USING btree ("tramKTTV_id");
 B   DROP INDEX public."thuyvan_songgiodongchay_tramKTTV_id_5bdc07d2";
       public            postgres    false    373            6           1259    85229 1   thuyvan_songgiodongchay_tramKTTV_id_5bdc07d2_like    INDEX     �   CREATE INDEX "thuyvan_songgiodongchay_tramKTTV_id_5bdc07d2_like" ON public.thuyvan_songgiodongchay USING btree ("tramKTTV_id" varchar_pattern_ops);
 G   DROP INDEX public."thuyvan_songgiodongchay_tramKTTV_id_5bdc07d2_like";
       public            postgres    false    373                       1259    85196 $   thuyvan_surface_baiboi_GM_Surface_id    INDEX     p   CREATE INDEX "thuyvan_surface_baiboi_GM_Surface_id" ON public.thuyvan_surface_baiboi USING gist ("GM_Surface");
 :   DROP INDEX public."thuyvan_surface_baiboi_GM_Surface_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    361                       1259    85195 /   thuyvan_surface_baiboi_maNhanDang_39ab4e57_like    INDEX     �   CREATE INDEX "thuyvan_surface_baiboi_maNhanDang_39ab4e57_like" ON public.thuyvan_surface_baiboi USING btree (manhandang varchar_pattern_ops);
 E   DROP INDEX public."thuyvan_surface_baiboi_maNhanDang_39ab4e57_like";
       public            postgres    false    361                       1259    85198 +   thuyvan_surface_baidaduoinuoc_GM_Surface_id    INDEX     ~   CREATE INDEX "thuyvan_surface_baidaduoinuoc_GM_Surface_id" ON public.thuyvan_surface_baidaduoinuoc USING gist ("GM_Surface");
 A   DROP INDEX public."thuyvan_surface_baidaduoinuoc_GM_Surface_id";
       public            postgres    false    362    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2                       1259    85197 6   thuyvan_surface_baidaduoinuoc_maNhanDang_1a4e425f_like    INDEX     �   CREATE INDEX "thuyvan_surface_baidaduoinuoc_maNhanDang_1a4e425f_like" ON public.thuyvan_surface_baidaduoinuoc USING btree (manhandang varchar_pattern_ops);
 L   DROP INDEX public."thuyvan_surface_baidaduoinuoc_maNhanDang_1a4e425f_like";
       public            postgres    false    362                       1259    85200 %   thuyvan_surface_biendao_GM_Surface_id    INDEX     r   CREATE INDEX "thuyvan_surface_biendao_GM_Surface_id" ON public.thuyvan_surface_biendao USING gist ("GM_Surface");
 ;   DROP INDEX public."thuyvan_surface_biendao_GM_Surface_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    363                       1259    85199 0   thuyvan_surface_biendao_maNhanDang_3dd815e7_like    INDEX     �   CREATE INDEX "thuyvan_surface_biendao_maNhanDang_3dd815e7_like" ON public.thuyvan_surface_biendao USING btree (manhandang varchar_pattern_ops);
 F   DROP INDEX public."thuyvan_surface_biendao_maNhanDang_3dd815e7_like";
       public            postgres    false    363                       1259    85202 !   thuyvan_surface_dao_GM_Surface_id    INDEX     j   CREATE INDEX "thuyvan_surface_dao_GM_Surface_id" ON public.thuyvan_surface_dao USING gist ("GM_Surface");
 7   DROP INDEX public."thuyvan_surface_dao_GM_Surface_id";
       public            postgres    false    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    364                       1259    85201 ,   thuyvan_surface_dao_maNhanDang_e9f562b5_like    INDEX     �   CREATE INDEX "thuyvan_surface_dao_maNhanDang_e9f562b5_like" ON public.thuyvan_surface_dao USING btree (manhandang varchar_pattern_ops);
 B   DROP INDEX public."thuyvan_surface_dao_maNhanDang_e9f562b5_like";
       public            postgres    false    364                       1259    85204 '   thuyvan_surface_kenhmuong_GM_Surface_id    INDEX     v   CREATE INDEX "thuyvan_surface_kenhmuong_GM_Surface_id" ON public.thuyvan_surface_kenhmuong USING gist ("GM_Surface");
 =   DROP INDEX public."thuyvan_surface_kenhmuong_GM_Surface_id";
       public            postgres    false    365    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2                        1259    85203 2   thuyvan_surface_kenhmuong_maNhanDang_50213ac1_like    INDEX     �   CREATE INDEX "thuyvan_surface_kenhmuong_maNhanDang_50213ac1_like" ON public.thuyvan_surface_kenhmuong USING btree (manhandang varchar_pattern_ops);
 H   DROP INDEX public."thuyvan_surface_kenhmuong_maNhanDang_50213ac1_like";
       public            postgres    false    365            #           1259    85206 '   thuyvan_surface_nguonnuoc_GM_Surface_id    INDEX     v   CREATE INDEX "thuyvan_surface_nguonnuoc_GM_Surface_id" ON public.thuyvan_surface_nguonnuoc USING gist ("GM_Surface");
 =   DROP INDEX public."thuyvan_surface_nguonnuoc_GM_Surface_id";
       public            postgres    false    366    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2            $           1259    85205 2   thuyvan_surface_nguonnuoc_maNhanDang_0c2c68c2_like    INDEX     �   CREATE INDEX "thuyvan_surface_nguonnuoc_maNhanDang_0c2c68c2_like" ON public.thuyvan_surface_nguonnuoc USING btree (manhandang varchar_pattern_ops);
 H   DROP INDEX public."thuyvan_surface_nguonnuoc_maNhanDang_0c2c68c2_like";
       public            postgres    false    366            1           1259    85221 '   thuyvan_thamsokttv_tramKTTV_id_dde17a98    INDEX     q   CREATE INDEX "thuyvan_thamsokttv_tramKTTV_id_dde17a98" ON public.thuyvan_thamsokttv USING btree ("tramKTTV_id");
 =   DROP INDEX public."thuyvan_thamsokttv_tramKTTV_id_dde17a98";
       public            postgres    false    371            2           1259    85222 ,   thuyvan_thamsokttv_tramKTTV_id_dde17a98_like    INDEX     �   CREATE INDEX "thuyvan_thamsokttv_tramKTTV_id_dde17a98_like" ON public.thuyvan_thamsokttv USING btree ("tramKTTV_id" varchar_pattern_ops);
 B   DROP INDEX public."thuyvan_thamsokttv_tramKTTV_id_dde17a98_like";
       public            postgres    false    371            -           1259    85214 '   thuyvan_thamsonuoc_tramKTTV_id_ca34ac26    INDEX     q   CREATE INDEX "thuyvan_thamsonuoc_tramKTTV_id_ca34ac26" ON public.thuyvan_thamsonuoc USING btree ("tramKTTV_id");
 =   DROP INDEX public."thuyvan_thamsonuoc_tramKTTV_id_ca34ac26";
       public            postgres    false    369            .           1259    85215 ,   thuyvan_thamsonuoc_tramKTTV_id_ca34ac26_like    INDEX     �   CREATE INDEX "thuyvan_thamsonuoc_tramKTTV_id_ca34ac26_like" ON public.thuyvan_thamsonuoc USING btree ("tramKTTV_id" varchar_pattern_ops);
 B   DROP INDEX public."thuyvan_thamsonuoc_tramKTTV_id_ca34ac26_like";
       public            postgres    false    369            '           1259    85208 #   thuyvan_tramthuthapkttv_GM_Point_id    INDEX     n   CREATE INDEX "thuyvan_tramthuthapkttv_GM_Point_id" ON public.thuyvan_tramthuthapkttv USING gist ("GM_Point");
 9   DROP INDEX public."thuyvan_tramthuthapkttv_GM_Point_id";
       public            postgres    false    367    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2    2            (           1259    85207 0   thuyvan_tramthuthapkttv_maNhanDang_bb22ec67_like    INDEX     �   CREATE INDEX "thuyvan_tramthuthapkttv_maNhanDang_bb22ec67_like" ON public.thuyvan_tramthuthapkttv USING btree (manhandang varchar_pattern_ops);
 F   DROP INDEX public."thuyvan_tramthuthapkttv_maNhanDang_bb22ec67_like";
       public            postgres    false    367            �           2606    85543 O   auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;
 y   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm;
       public          postgres    false    4530    211    377            �           2606    85538 P   auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 z   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id;
       public          postgres    false    375    5179    377            S           2606    83382 E   auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 o   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co;
       public          postgres    false    4525    211    209            c           2606    84144 _   dancu_curve_congtrinhcongnghiep dancu_curve_congtrin_congtrinhcongnghiep__11feb931_fk_dancu_con    FK CONSTRAINT       ALTER TABLE ONLY public.dancu_curve_congtrinhcongnghiep
    ADD CONSTRAINT dancu_curve_congtrin_congtrinhcongnghiep__11feb931_fk_dancu_con FOREIGN KEY (congtrinhcongnghiep_ptr_id) REFERENCES public.dancu_congtrinhcongnghiep(manhandang) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.dancu_curve_congtrinhcongnghiep DROP CONSTRAINT dancu_curve_congtrin_congtrinhcongnghiep__11feb931_fk_dancu_con;
       public          postgres    false    276    236    4623            d           2606    84151 _   dancu_point_congtrinhcongnghiep dancu_point_congtrin_congtrinhcongnghiep__5ca14438_fk_dancu_con    FK CONSTRAINT       ALTER TABLE ONLY public.dancu_point_congtrinhcongnghiep
    ADD CONSTRAINT dancu_point_congtrin_congtrinhcongnghiep__5ca14438_fk_dancu_con FOREIGN KEY (congtrinhcongnghiep_ptr_id) REFERENCES public.dancu_congtrinhcongnghiep(manhandang) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.dancu_point_congtrinhcongnghiep DROP CONSTRAINT dancu_point_congtrin_congtrinhcongnghiep__5ca14438_fk_dancu_con;
       public          postgres    false    4623    236    277            e           2606    84158 a   dancu_surface_congtrinhcongnghiep dancu_surface_congtr_congtrinhcongnghiep__91d937a2_fk_dancu_con    FK CONSTRAINT       ALTER TABLE ONLY public.dancu_surface_congtrinhcongnghiep
    ADD CONSTRAINT dancu_surface_congtr_congtrinhcongnghiep__91d937a2_fk_dancu_con FOREIGN KEY (congtrinhcongnghiep_ptr_id) REFERENCES public.dancu_congtrinhcongnghiep(manhandang) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.dancu_surface_congtrinhcongnghiep DROP CONSTRAINT dancu_surface_congtr_congtrinhcongnghiep__91d937a2_fk_dancu_con;
       public          postgres    false    236    278    4623            f           2606    84326 C   diahinh_solieuhkdc diahinh_solieuhkdc_HKDC_id_5a8d313c_fk_diahinh_h    FK CONSTRAINT     �   ALTER TABLE ONLY public.diahinh_solieuhkdc
    ADD CONSTRAINT "diahinh_solieuhkdc_HKDC_id_5a8d313c_fk_diahinh_h" FOREIGN KEY ("HKDC_id") REFERENCES public.diahinh_hokhoandiachat(manhandang) DEFERRABLE INITIALLY DEFERRED;
 o   ALTER TABLE ONLY public.diahinh_solieuhkdc DROP CONSTRAINT "diahinh_solieuhkdc_HKDC_id_5a8d313c_fk_diahinh_h";
       public          postgres    false    286    295    4823            a           2606    83637 G   django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co    FK CONSTRAINT     �   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 q   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co;
       public          postgres    false    4525    228    209            b           2606    83643 P   django_admin_log django_admin_log_user_id_c564eba6_fk_dulieuquantri_nguoidung_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_dulieuquantri_nguoidung_id FOREIGN KEY (user_id) REFERENCES public.dulieuquantri_nguoidung(id) DEFERRABLE INITIALLY DEFERRED;
 z   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_user_id_c564eba6_fk_dulieuquantri_nguoidung_id;
       public          postgres    false    222    4573    228            T           2606    83483 P   dulieuquantri_bienchetrangbi dulieuquantri_biench_donVi_id_b4f1eda2_fk_dulieuqua    FK CONSTRAINT     �   ALTER TABLE ONLY public.dulieuquantri_bienchetrangbi
    ADD CONSTRAINT "dulieuquantri_biench_donVi_id_b4f1eda2_fk_dulieuqua" FOREIGN KEY ("donVi_id") REFERENCES public.dulieuquantri_donvi("maNhanDang") DEFERRABLE INITIALLY DEFERRED;
 |   ALTER TABLE ONLY public.dulieuquantri_bienchetrangbi DROP CONSTRAINT "dulieuquantri_biench_donVi_id_b4f1eda2_fk_dulieuqua";
       public          postgres    false    4569    220    212            V           2606    100019 \   dulieuquantri_bienchetrangbi dulieuquantri_biench_loaiTrangBiKhiTai_id_3651cca4_fk_dulieuqua    FK CONSTRAINT       ALTER TABLE ONLY public.dulieuquantri_bienchetrangbi
    ADD CONSTRAINT "dulieuquantri_biench_loaiTrangBiKhiTai_id_3651cca4_fk_dulieuqua" FOREIGN KEY ("loaiTrangBiKhiTai_id") REFERENCES public.dulieuquantri_loaitrangbikhitai("maNhanDang") DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.dulieuquantri_bienchetrangbi DROP CONSTRAINT "dulieuquantri_biench_loaiTrangBiKhiTai_id_3651cca4_fk_dulieuqua";
       public          postgres    false    215    4550    212            W           2606    100024 [   dulieuquantri_bienchetrangbi dulieuquantri_biench_tinhTrangTrangBi_id_a5a6d3a1_fk_dulieuqua    FK CONSTRAINT       ALTER TABLE ONLY public.dulieuquantri_bienchetrangbi
    ADD CONSTRAINT "dulieuquantri_biench_tinhTrangTrangBi_id_a5a6d3a1_fk_dulieuqua" FOREIGN KEY ("tinhTrangTrangBi_id") REFERENCES public.dulieuquantri_tinhtrangtrangbi("maNhanDang") DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.dulieuquantri_bienchetrangbi DROP CONSTRAINT "dulieuquantri_biench_tinhTrangTrangBi_id_a5a6d3a1_fk_dulieuqua";
       public          postgres    false    212    216    4553            U           2606    83498 Q   dulieuquantri_bienchetrangbi dulieuquantri_biench_xuatXu_id_d700e72f_fk_dulieuqua    FK CONSTRAINT     �   ALTER TABLE ONLY public.dulieuquantri_bienchetrangbi
    ADD CONSTRAINT "dulieuquantri_biench_xuatXu_id_d700e72f_fk_dulieuqua" FOREIGN KEY ("xuatXu_id") REFERENCES public.dulieuquantri_xuatxu("maNhanDang") DEFERRABLE INITIALLY DEFERRED;
 }   ALTER TABLE ONLY public.dulieuquantri_bienchetrangbi DROP CONSTRAINT "dulieuquantri_biench_xuatXu_id_d700e72f_fk_dulieuqua";
       public          postgres    false    4556    212    217            Y           2606    91807 E   dulieuquantri_donvi dulieuquantri_donvi_CTQP_id_32ca9ea7_fk_dancu_poi    FK CONSTRAINT     �   ALTER TABLE ONLY public.dulieuquantri_donvi
    ADD CONSTRAINT "dulieuquantri_donvi_CTQP_id_32ca9ea7_fk_dancu_poi" FOREIGN KEY ("CTQP_id") REFERENCES public.dancu_point_congtrinhquocphong(manhandang) DEFERRABLE INITIALLY DEFERRED;
 q   ALTER TABLE ONLY public.dulieuquantri_donvi DROP CONSTRAINT "dulieuquantri_donvi_CTQP_id_32ca9ea7_fk_dancu_poi";
       public          postgres    false    220    247    4667            Z           2606    91812 I   dulieuquantri_donvi dulieuquantri_donvi_capDonVi_id_7bae2bf4_fk_dulieuqua    FK CONSTRAINT     �   ALTER TABLE ONLY public.dulieuquantri_donvi
    ADD CONSTRAINT "dulieuquantri_donvi_capDonVi_id_7bae2bf4_fk_dulieuqua" FOREIGN KEY ("capDonVi_id") REFERENCES public.dulieuquantri_capdonvi("maNhanDang") DEFERRABLE INITIALLY DEFERRED;
 u   ALTER TABLE ONLY public.dulieuquantri_donvi DROP CONSTRAINT "dulieuquantri_donvi_capDonVi_id_7bae2bf4_fk_dulieuqua";
       public          postgres    false    220    4544    213            [           2606    91817 J   dulieuquantri_donvi dulieuquantri_donvi_loaiDonVi_id_83857109_fk_dulieuqua    FK CONSTRAINT     �   ALTER TABLE ONLY public.dulieuquantri_donvi
    ADD CONSTRAINT "dulieuquantri_donvi_loaiDonVi_id_83857109_fk_dulieuqua" FOREIGN KEY ("loaiDonVi_id") REFERENCES public.dulieuquantri_loaidonvi("maNhanDang") DEFERRABLE INITIALLY DEFERRED;
 v   ALTER TABLE ONLY public.dulieuquantri_donvi DROP CONSTRAINT "dulieuquantri_donvi_loaiDonVi_id_83857109_fk_dulieuqua";
       public          postgres    false    4547    220    214            \           2606    83589 K   dulieuquantri_nguoidung dulieuquantri_nguoid_donVi_id_96e959e6_fk_dulieuqua    FK CONSTRAINT     �   ALTER TABLE ONLY public.dulieuquantri_nguoidung
    ADD CONSTRAINT "dulieuquantri_nguoid_donVi_id_96e959e6_fk_dulieuqua" FOREIGN KEY ("donVi_id") REFERENCES public.dulieuquantri_donvi("maNhanDang") DEFERRABLE INITIALLY DEFERRED;
 w   ALTER TABLE ONLY public.dulieuquantri_nguoidung DROP CONSTRAINT "dulieuquantri_nguoid_donVi_id_96e959e6_fk_dulieuqua";
       public          postgres    false    222    4569    220            ^           2606    85550 R   dulieuquantri_nguoidung_groups dulieuquantri_nguoid_group_id_d858ede1_fk_auth_grou    FK CONSTRAINT     �   ALTER TABLE ONLY public.dulieuquantri_nguoidung_groups
    ADD CONSTRAINT dulieuquantri_nguoid_group_id_d858ede1_fk_auth_grou FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 |   ALTER TABLE ONLY public.dulieuquantri_nguoidung_groups DROP CONSTRAINT dulieuquantri_nguoid_group_id_d858ede1_fk_auth_grou;
       public          postgres    false    5179    224    375            ]           2606    83599 V   dulieuquantri_nguoidung_groups dulieuquantri_nguoid_nguoidung_id_347564d5_fk_dulieuqua    FK CONSTRAINT     �   ALTER TABLE ONLY public.dulieuquantri_nguoidung_groups
    ADD CONSTRAINT dulieuquantri_nguoid_nguoidung_id_347564d5_fk_dulieuqua FOREIGN KEY (nguoidung_id) REFERENCES public.dulieuquantri_nguoidung(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.dulieuquantri_nguoidung_groups DROP CONSTRAINT dulieuquantri_nguoid_nguoidung_id_347564d5_fk_dulieuqua;
       public          postgres    false    4573    222    224            _           2606    83613 `   dulieuquantri_nguoidung_user_permissions dulieuquantri_nguoid_nguoidung_id_4a884827_fk_dulieuqua    FK CONSTRAINT     �   ALTER TABLE ONLY public.dulieuquantri_nguoidung_user_permissions
    ADD CONSTRAINT dulieuquantri_nguoid_nguoidung_id_4a884827_fk_dulieuqua FOREIGN KEY (nguoidung_id) REFERENCES public.dulieuquantri_nguoidung(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.dulieuquantri_nguoidung_user_permissions DROP CONSTRAINT dulieuquantri_nguoid_nguoidung_id_4a884827_fk_dulieuqua;
       public          postgres    false    222    226    4573            `           2606    83618 a   dulieuquantri_nguoidung_user_permissions dulieuquantri_nguoid_permission_id_4f784da8_fk_auth_perm    FK CONSTRAINT     �   ALTER TABLE ONLY public.dulieuquantri_nguoidung_user_permissions
    ADD CONSTRAINT dulieuquantri_nguoid_permission_id_4f784da8_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.dulieuquantri_nguoidung_user_permissions DROP CONSTRAINT dulieuquantri_nguoid_permission_id_4f784da8_fk_auth_perm;
       public          postgres    false    226    4530    211            X           2606    85555 X   dulieuquantri_nhomtaikhoan dulieuquantri_nhomtaikhoan_group_id_78d473d5_fk_auth_group_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.dulieuquantri_nhomtaikhoan
    ADD CONSTRAINT dulieuquantri_nhomtaikhoan_group_id_78d473d5_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.dulieuquantri_nhomtaikhoan DROP CONSTRAINT dulieuquantri_nhomtaikhoan_group_id_78d473d5_fk_auth_group_id;
       public          postgres    false    219    375    5179            �           2606    91853 S   dulieuquantri_thietbikhitai dulieuquantri_thietb_bienCheTB_id_9721a570_fk_dulieuqua    FK CONSTRAINT     �   ALTER TABLE ONLY public.dulieuquantri_thietbikhitai
    ADD CONSTRAINT "dulieuquantri_thietb_bienCheTB_id_9721a570_fk_dulieuqua" FOREIGN KEY ("bienCheTB_id") REFERENCES public.dulieuquantri_bienchetrangbi("maNhanDang") DEFERRABLE INITIALLY DEFERRED;
    ALTER TABLE ONLY public.dulieuquantri_thietbikhitai DROP CONSTRAINT "dulieuquantri_thietb_bienCheTB_id_9721a570_fk_dulieuqua";
       public          postgres    false    4537    380    212            �           2606    91838 [   dulieuquantri_thietbikhitai dulieuquantri_thietb_loaiTrangBiKhiTai_id_0dd84a5c_fk_dulieuqua    FK CONSTRAINT       ALTER TABLE ONLY public.dulieuquantri_thietbikhitai
    ADD CONSTRAINT "dulieuquantri_thietb_loaiTrangBiKhiTai_id_0dd84a5c_fk_dulieuqua" FOREIGN KEY ("loaiTrangBiKhiTai_id") REFERENCES public.dulieuquantri_loaitrangbikhitai("maNhanDang") DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.dulieuquantri_thietbikhitai DROP CONSTRAINT "dulieuquantri_thietb_loaiTrangBiKhiTai_id_0dd84a5c_fk_dulieuqua";
       public          postgres    false    215    380    4550            �           2606    91843 Z   dulieuquantri_thietbikhitai dulieuquantri_thietb_tinhTrangTrangBi_id_d012e038_fk_dulieuqua    FK CONSTRAINT     
  ALTER TABLE ONLY public.dulieuquantri_thietbikhitai
    ADD CONSTRAINT "dulieuquantri_thietb_tinhTrangTrangBi_id_d012e038_fk_dulieuqua" FOREIGN KEY ("tinhTrangTrangBi_id") REFERENCES public.dulieuquantri_tinhtrangtrangbi("maNhanDang") DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.dulieuquantri_thietbikhitai DROP CONSTRAINT "dulieuquantri_thietb_tinhTrangTrangBi_id_d012e038_fk_dulieuqua";
       public          postgres    false    4553    216    380            �           2606    91848 P   dulieuquantri_thietbikhitai dulieuquantri_thietb_xuatXu_id_3f8b8ee6_fk_dulieuqua    FK CONSTRAINT     �   ALTER TABLE ONLY public.dulieuquantri_thietbikhitai
    ADD CONSTRAINT "dulieuquantri_thietb_xuatXu_id_3f8b8ee6_fk_dulieuqua" FOREIGN KEY ("xuatXu_id") REFERENCES public.dulieuquantri_xuatxu("maNhanDang") DEFERRABLE INITIALLY DEFERRED;
 |   ALTER TABLE ONLY public.dulieuquantri_thietbikhitai DROP CONSTRAINT "dulieuquantri_thietb_xuatXu_id_3f8b8ee6_fk_dulieuqua";
       public          postgres    false    380    4556    217            h           2606    84399 O   eav_attribute_entity_ct eav_attribute_entity_attribute_id_384edb80_fk_eav_attri    FK CONSTRAINT     �   ALTER TABLE ONLY public.eav_attribute_entity_ct
    ADD CONSTRAINT eav_attribute_entity_attribute_id_384edb80_fk_eav_attri FOREIGN KEY (attribute_id) REFERENCES public.eav_attribute(id) DEFERRABLE INITIALLY DEFERRED;
 y   ALTER TABLE ONLY public.eav_attribute_entity_ct DROP CONSTRAINT eav_attribute_entity_attribute_id_384edb80_fk_eav_attri;
       public          postgres    false    4858    299    297            i           2606    84404 Q   eav_attribute_entity_ct eav_attribute_entity_contenttype_id_6a747efe_fk_django_co    FK CONSTRAINT     �   ALTER TABLE ONLY public.eav_attribute_entity_ct
    ADD CONSTRAINT eav_attribute_entity_contenttype_id_6a747efe_fk_django_co FOREIGN KEY (contenttype_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 {   ALTER TABLE ONLY public.eav_attribute_entity_ct DROP CONSTRAINT eav_attribute_entity_contenttype_id_6a747efe_fk_django_co;
       public          postgres    false    4525    299    209            g           2606    84391 F   eav_attribute eav_attribute_enum_group_id_47628614_fk_eav_enumgroup_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.eav_attribute
    ADD CONSTRAINT eav_attribute_enum_group_id_47628614_fk_eav_enumgroup_id FOREIGN KEY (enum_group_id) REFERENCES public.eav_enumgroup(id) DEFERRABLE INITIALLY DEFERRED;
 p   ALTER TABLE ONLY public.eav_attribute DROP CONSTRAINT eav_attribute_enum_group_id_47628614_fk_eav_enumgroup_id;
       public          postgres    false    305    4883    297            n           2606    84439 S   eav_enumgroup_values eav_enumgroup_values_enumgroup_id_2bdd7858_fk_eav_enumgroup_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.eav_enumgroup_values
    ADD CONSTRAINT eav_enumgroup_values_enumgroup_id_2bdd7858_fk_eav_enumgroup_id FOREIGN KEY (enumgroup_id) REFERENCES public.eav_enumgroup(id) DEFERRABLE INITIALLY DEFERRED;
 }   ALTER TABLE ONLY public.eav_enumgroup_values DROP CONSTRAINT eav_enumgroup_values_enumgroup_id_2bdd7858_fk_eav_enumgroup_id;
       public          postgres    false    4883    305    307            o           2606    84444 S   eav_enumgroup_values eav_enumgroup_values_enumvalue_id_52f83e3a_fk_eav_enumvalue_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.eav_enumgroup_values
    ADD CONSTRAINT eav_enumgroup_values_enumvalue_id_52f83e3a_fk_eav_enumvalue_id FOREIGN KEY (enumvalue_id) REFERENCES public.eav_enumvalue(id) DEFERRABLE INITIALLY DEFERRED;
 }   ALTER TABLE ONLY public.eav_enumgroup_values DROP CONSTRAINT eav_enumgroup_values_enumvalue_id_52f83e3a_fk_eav_enumvalue_id;
       public          postgres    false    307    301    4869            j           2606    84412 =   eav_value eav_value_attribute_id_6fd472ba_fk_eav_attribute_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.eav_value
    ADD CONSTRAINT eav_value_attribute_id_6fd472ba_fk_eav_attribute_id FOREIGN KEY (attribute_id) REFERENCES public.eav_attribute(id) DEFERRABLE INITIALLY DEFERRED;
 g   ALTER TABLE ONLY public.eav_value DROP CONSTRAINT eav_value_attribute_id_6fd472ba_fk_eav_attribute_id;
       public          postgres    false    4858    297    303            k           2606    84417 C   eav_value eav_value_entity_ct_id_5cfd530e_fk_django_content_type_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.eav_value
    ADD CONSTRAINT eav_value_entity_ct_id_5cfd530e_fk_django_content_type_id FOREIGN KEY (entity_ct_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 m   ALTER TABLE ONLY public.eav_value DROP CONSTRAINT eav_value_entity_ct_id_5cfd530e_fk_django_content_type_id;
       public          postgres    false    4525    303    209            l           2606    84422 =   eav_value eav_value_generic_value_ct_id_d4681436_fk_django_co    FK CONSTRAINT     �   ALTER TABLE ONLY public.eav_value
    ADD CONSTRAINT eav_value_generic_value_ct_id_d4681436_fk_django_co FOREIGN KEY (generic_value_ct_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 g   ALTER TABLE ONLY public.eav_value DROP CONSTRAINT eav_value_generic_value_ct_id_d4681436_fk_django_co;
       public          postgres    false    209    303    4525            m           2606    84427 >   eav_value eav_value_value_enum_id_86e48f74_fk_eav_enumvalue_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.eav_value
    ADD CONSTRAINT eav_value_value_enum_id_86e48f74_fk_eav_enumvalue_id FOREIGN KEY (value_enum_id) REFERENCES public.eav_enumvalue(id) DEFERRABLE INITIALLY DEFERRED;
 h   ALTER TABLE ONLY public.eav_value DROP CONSTRAINT eav_value_value_enum_id_86e48f74_fk_eav_enumvalue_id;
       public          postgres    false    301    303    4869            u           2606    85613 Q   multimedia_dulieudaphuongtien multimedia_dulieudap_lopDL_id_dca210f1_fk_multimedi    FK CONSTRAINT     �   ALTER TABLE ONLY public.multimedia_dulieudaphuongtien
    ADD CONSTRAINT "multimedia_dulieudap_lopDL_id_dca210f1_fk_multimedi" FOREIGN KEY ("lopDL_id") REFERENCES public.multimedia_lopdulieu("maNhanDang") DEFERRABLE INITIALLY DEFERRED;
 }   ALTER TABLE ONLY public.multimedia_dulieudaphuongtien DROP CONSTRAINT "multimedia_dulieudap_lopDL_id_dca210f1_fk_multimedi";
       public          postgres    false    323    4955    327            q           2606    87132 O   multimedia_lopdulieu multimedia_lopdulieu_content_type_id_afad65b4_fk_django_co    FK CONSTRAINT     �   ALTER TABLE ONLY public.multimedia_lopdulieu
    ADD CONSTRAINT multimedia_lopdulieu_content_type_id_afad65b4_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 y   ALTER TABLE ONLY public.multimedia_lopdulieu DROP CONSTRAINT multimedia_lopdulieu_content_type_id_afad65b4_fk_django_co;
       public          postgres    false    209    323    4525            p           2606    85618 I   multimedia_lopdulieu multimedia_lopdulieu_nhomDL_id_434b279d_fk_multimedi    FK CONSTRAINT     �   ALTER TABLE ONLY public.multimedia_lopdulieu
    ADD CONSTRAINT "multimedia_lopdulieu_nhomDL_id_434b279d_fk_multimedi" FOREIGN KEY ("nhomDL_id") REFERENCES public.multimedia_nhomdulieu("maNhanDang") DEFERRABLE INITIALLY DEFERRED;
 u   ALTER TABLE ONLY public.multimedia_lopdulieu DROP CONSTRAINT "multimedia_lopdulieu_nhomDL_id_434b279d_fk_multimedi";
       public          postgres    false    323    4958    324            t           2606    85608 <   multimedia_metadata multimedia_metadata_maLop_id_85a23344_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.multimedia_metadata
    ADD CONSTRAINT "multimedia_metadata_maLop_id_85a23344_fk" FOREIGN KEY ("maLop_id") REFERENCES public.multimedia_lopdulieu("maNhanDang") DEFERRABLE INITIALLY DEFERRED;
 h   ALTER TABLE ONLY public.multimedia_metadata DROP CONSTRAINT "multimedia_metadata_maLop_id_85a23344_fk";
       public          postgres    false    323    4955    326            r           2606    84642 F   multimedia_style multimedia_style_maLoaiStyle_id_4a70fe18_fk_multimedi    FK CONSTRAINT     �   ALTER TABLE ONLY public.multimedia_style
    ADD CONSTRAINT "multimedia_style_maLoaiStyle_id_4a70fe18_fk_multimedi" FOREIGN KEY ("maLoaiStyle_id") REFERENCES public.multimedia_loaistyle("maNhanDang") DEFERRABLE INITIALLY DEFERRED;
 r   ALTER TABLE ONLY public.multimedia_style DROP CONSTRAINT "multimedia_style_maLoaiStyle_id_4a70fe18_fk_multimedi";
       public          postgres    false    322    4948    325            s           2606    85598 6   multimedia_style multimedia_style_maLop_id_62c9d9bd_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.multimedia_style
    ADD CONSTRAINT "multimedia_style_maLop_id_62c9d9bd_fk" FOREIGN KEY ("maLop_id") REFERENCES public.multimedia_lopdulieu("maNhanDang") DEFERRABLE INITIALLY DEFERRED;
 b   ALTER TABLE ONLY public.multimedia_style DROP CONSTRAINT "multimedia_style_maLop_id_62c9d9bd_fk";
       public          postgres    false    323    4955    325            �           2606    84993 K   soanthaokehoach_diemnvdh soanthaokehoach_diem_nvdh_id_0036ead6_fk_soanthaok    FK CONSTRAINT     �   ALTER TABLE ONLY public.soanthaokehoach_diemnvdh
    ADD CONSTRAINT soanthaokehoach_diem_nvdh_id_0036ead6_fk_soanthaok FOREIGN KEY (nvdh_id) REFERENCES public.soanthaokehoach_nvdh("maNhanDang") DEFERRABLE INITIALLY DEFERRED;
 u   ALTER TABLE ONLY public.soanthaokehoach_diemnvdh DROP CONSTRAINT soanthaokehoach_diem_nvdh_id_0036ead6_fk_soanthaok;
       public          postgres    false    5026    349    338            v           2606    84864 M   soanthaokehoach_ganlucluong soanthaokehoach_ganl_pat_id_c136a398_fk_soanthaok    FK CONSTRAINT     �   ALTER TABLE ONLY public.soanthaokehoach_ganlucluong
    ADD CONSTRAINT soanthaokehoach_ganl_pat_id_c136a398_fk_soanthaok FOREIGN KEY (pat_id) REFERENCES public.soanthaokehoach_phuongantuyen("maNhanDang") DEFERRABLE INITIALLY DEFERRED;
 w   ALTER TABLE ONLY public.soanthaokehoach_ganlucluong DROP CONSTRAINT soanthaokehoach_ganl_pat_id_c136a398_fk_soanthaok;
       public          postgres    false    343    336    5056            w           2606    84869 M   soanthaokehoach_ganlucluong soanthaokehoach_ganl_pav_id_5589b6c1_fk_soanthaok    FK CONSTRAINT     �   ALTER TABLE ONLY public.soanthaokehoach_ganlucluong
    ADD CONSTRAINT soanthaokehoach_ganl_pav_id_5589b6c1_fk_soanthaok FOREIGN KEY (pav_id) REFERENCES public.soanthaokehoach_phuonganvung("maNhanDang") DEFERRABLE INITIALLY DEFERRED;
 w   ALTER TABLE ONLY public.soanthaokehoach_ganlucluong DROP CONSTRAINT soanthaokehoach_ganl_pav_id_5589b6c1_fk_soanthaok;
       public          postgres    false    5044    336    341            x           2606    84874 N   soanthaokehoach_ganlucluong soanthaokehoach_ganl_pavt_id_704f22bd_fk_soanthaok    FK CONSTRAINT     �   ALTER TABLE ONLY public.soanthaokehoach_ganlucluong
    ADD CONSTRAINT soanthaokehoach_ganl_pavt_id_704f22bd_fk_soanthaok FOREIGN KEY (pavt_id) REFERENCES public.soanthaokehoach_phuonganvitri("maNhanDang") DEFERRABLE INITIALLY DEFERRED;
 x   ALTER TABLE ONLY public.soanthaokehoach_ganlucluong DROP CONSTRAINT soanthaokehoach_ganl_pavt_id_704f22bd_fk_soanthaok;
       public          postgres    false    342    5050    336            z           2606    84888 G   soanthaokehoach_nvbp soanthaokehoach_nvbp_maDV_id_87b2c8ac_fk_dulieuqua    FK CONSTRAINT     �   ALTER TABLE ONLY public.soanthaokehoach_nvbp
    ADD CONSTRAINT "soanthaokehoach_nvbp_maDV_id_87b2c8ac_fk_dulieuqua" FOREIGN KEY ("maDV_id") REFERENCES public.dulieuquantri_donvi("maNhanDang") DEFERRABLE INITIALLY DEFERRED;
 s   ALTER TABLE ONLY public.soanthaokehoach_nvbp DROP CONSTRAINT "soanthaokehoach_nvbp_maDV_id_87b2c8ac_fk_dulieuqua";
       public          postgres    false    4569    337    220            y           2606    84859 I   soanthaokehoach_nvbp soanthaokehoach_nvbp_maNVDH_id_9bf11f77_fk_soanthaok    FK CONSTRAINT     �   ALTER TABLE ONLY public.soanthaokehoach_nvbp
    ADD CONSTRAINT "soanthaokehoach_nvbp_maNVDH_id_9bf11f77_fk_soanthaok" FOREIGN KEY ("maNVDH_id") REFERENCES public.soanthaokehoach_nvdh("maNhanDang") DEFERRABLE INITIALLY DEFERRED;
 u   ALTER TABLE ONLY public.soanthaokehoach_nvbp DROP CONSTRAINT "soanthaokehoach_nvbp_maNVDH_id_9bf11f77_fk_soanthaok";
       public          postgres    false    5026    337    338            �           2606    84969 _   soanthaokehoach_pheduyetphuonganganlucluong soanthaokehoach_phed_ganLL_id_c3cec84e_fk_soanthaok    FK CONSTRAINT       ALTER TABLE ONLY public.soanthaokehoach_pheduyetphuonganganlucluong
    ADD CONSTRAINT "soanthaokehoach_phed_ganLL_id_c3cec84e_fk_soanthaok" FOREIGN KEY ("ganLL_id") REFERENCES public.soanthaokehoach_ganlucluong("maNhanDang") DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.soanthaokehoach_pheduyetphuonganganlucluong DROP CONSTRAINT "soanthaokehoach_phed_ganLL_id_c3cec84e_fk_soanthaok";
       public          postgres    false    5016    347    336            �           2606    84977 T   soanthaokehoach_pheduyetchungnvbp soanthaokehoach_phed_nvbp_id_d82658f9_fk_soanthaok    FK CONSTRAINT     �   ALTER TABLE ONLY public.soanthaokehoach_pheduyetchungnvbp
    ADD CONSTRAINT soanthaokehoach_phed_nvbp_id_d82658f9_fk_soanthaok FOREIGN KEY (nvbp_id) REFERENCES public.soanthaokehoach_nvbp("maNhanDang") DEFERRABLE INITIALLY DEFERRED;
 ~   ALTER TABLE ONLY public.soanthaokehoach_pheduyetchungnvbp DROP CONSTRAINT soanthaokehoach_phed_nvbp_id_d82658f9_fk_soanthaok;
       public          postgres    false    348    337    5023            �           2606    84960 [   soanthaokehoach_pheduyetphuongantuyen soanthaokehoach_phed_paTuyen_id_cea8cdf2_fk_soanthaok    FK CONSTRAINT       ALTER TABLE ONLY public.soanthaokehoach_pheduyetphuongantuyen
    ADD CONSTRAINT "soanthaokehoach_phed_paTuyen_id_cea8cdf2_fk_soanthaok" FOREIGN KEY ("paTuyen_id") REFERENCES public.soanthaokehoach_phuongantuyen("maNhanDang") DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.soanthaokehoach_pheduyetphuongantuyen DROP CONSTRAINT "soanthaokehoach_phed_paTuyen_id_cea8cdf2_fk_soanthaok";
       public          postgres    false    346    5056    343            �           2606    84951 [   soanthaokehoach_pheduyetphuonganvitri soanthaokehoach_phed_paViTri_id_996e5b8f_fk_soanthaok    FK CONSTRAINT       ALTER TABLE ONLY public.soanthaokehoach_pheduyetphuonganvitri
    ADD CONSTRAINT "soanthaokehoach_phed_paViTri_id_996e5b8f_fk_soanthaok" FOREIGN KEY ("paViTri_id") REFERENCES public.soanthaokehoach_phuonganvitri("maNhanDang") DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.soanthaokehoach_pheduyetphuonganvitri DROP CONSTRAINT "soanthaokehoach_phed_paViTri_id_996e5b8f_fk_soanthaok";
       public          postgres    false    342    345    5050            �           2606    84942 Y   soanthaokehoach_pheduyetphuonganvung soanthaokehoach_phed_paVung_id_07d3ee65_fk_soanthaok    FK CONSTRAINT     �   ALTER TABLE ONLY public.soanthaokehoach_pheduyetphuonganvung
    ADD CONSTRAINT "soanthaokehoach_phed_paVung_id_07d3ee65_fk_soanthaok" FOREIGN KEY ("paVung_id") REFERENCES public.soanthaokehoach_phuonganvung("maNhanDang") DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.soanthaokehoach_pheduyetphuonganvung DROP CONSTRAINT "soanthaokehoach_phed_paVung_id_07d3ee65_fk_soanthaok";
       public          postgres    false    344    5044    341                       2606    84933 P   soanthaokehoach_phuongantuyen soanthaokehoach_phuo_nvbp_id_133e3389_fk_soanthaok    FK CONSTRAINT     �   ALTER TABLE ONLY public.soanthaokehoach_phuongantuyen
    ADD CONSTRAINT soanthaokehoach_phuo_nvbp_id_133e3389_fk_soanthaok FOREIGN KEY (nvbp_id) REFERENCES public.soanthaokehoach_nvbp("maNhanDang") DEFERRABLE INITIALLY DEFERRED;
 z   ALTER TABLE ONLY public.soanthaokehoach_phuongantuyen DROP CONSTRAINT soanthaokehoach_phuo_nvbp_id_133e3389_fk_soanthaok;
       public          postgres    false    5023    337    343            }           2606    84915 O   soanthaokehoach_phuonganvung soanthaokehoach_phuo_nvbp_id_a105a16e_fk_soanthaok    FK CONSTRAINT     �   ALTER TABLE ONLY public.soanthaokehoach_phuonganvung
    ADD CONSTRAINT soanthaokehoach_phuo_nvbp_id_a105a16e_fk_soanthaok FOREIGN KEY (nvbp_id) REFERENCES public.soanthaokehoach_nvbp("maNhanDang") DEFERRABLE INITIALLY DEFERRED;
 y   ALTER TABLE ONLY public.soanthaokehoach_phuonganvung DROP CONSTRAINT soanthaokehoach_phuo_nvbp_id_a105a16e_fk_soanthaok;
       public          postgres    false    337    5023    341            ~           2606    84924 P   soanthaokehoach_phuonganvitri soanthaokehoach_phuo_nvbp_id_c1e6acb3_fk_soanthaok    FK CONSTRAINT     �   ALTER TABLE ONLY public.soanthaokehoach_phuonganvitri
    ADD CONSTRAINT soanthaokehoach_phuo_nvbp_id_c1e6acb3_fk_soanthaok FOREIGN KEY (nvbp_id) REFERENCES public.soanthaokehoach_nvbp("maNhanDang") DEFERRABLE INITIALLY DEFERRED;
 z   ALTER TABLE ONLY public.soanthaokehoach_phuonganvitri DROP CONSTRAINT soanthaokehoach_phuo_nvbp_id_c1e6acb3_fk_soanthaok;
       public          postgres    false    337    5023    342            |           2606    84906 L   soanthaokehoach_tuyennvdh soanthaokehoach_tuye_nvdh_id_094789c0_fk_soanthaok    FK CONSTRAINT     �   ALTER TABLE ONLY public.soanthaokehoach_tuyennvdh
    ADD CONSTRAINT soanthaokehoach_tuye_nvdh_id_094789c0_fk_soanthaok FOREIGN KEY (nvdh_id) REFERENCES public.soanthaokehoach_nvdh("maNhanDang") DEFERRABLE INITIALLY DEFERRED;
 v   ALTER TABLE ONLY public.soanthaokehoach_tuyennvdh DROP CONSTRAINT soanthaokehoach_tuye_nvdh_id_094789c0_fk_soanthaok;
       public          postgres    false    5026    338    340            {           2606    84897 K   soanthaokehoach_vungnvdh soanthaokehoach_vung_nvdh_id_cc249707_fk_soanthaok    FK CONSTRAINT     �   ALTER TABLE ONLY public.soanthaokehoach_vungnvdh
    ADD CONSTRAINT soanthaokehoach_vung_nvdh_id_cc249707_fk_soanthaok FOREIGN KEY (nvdh_id) REFERENCES public.soanthaokehoach_nvdh("maNhanDang") DEFERRABLE INITIALLY DEFERRED;
 u   ALTER TABLE ONLY public.soanthaokehoach_vungnvdh DROP CONSTRAINT soanthaokehoach_vung_nvdh_id_cc249707_fk_soanthaok;
       public          postgres    false    5026    339    338            �           2606    85640 9   test_mymodel test_mymodel_choice_id_14e4a959_fk_test_usec    FK CONSTRAINT     �   ALTER TABLE ONLY public.test_mymodel
    ADD CONSTRAINT test_mymodel_choice_id_14e4a959_fk_test_usec FOREIGN KEY (choice_id) REFERENCES public.test_usecontenttype("maNhanDang_id") DEFERRABLE INITIALLY DEFERRED;
 c   ALTER TABLE ONLY public.test_mymodel DROP CONSTRAINT test_mymodel_choice_id_14e4a959_fk_test_usec;
       public          postgres    false    378    5187    379            �           2606    85565 K   test_usecontenttype test_usecontenttype_maNhanDang_id_fc0aa097_fk_django_co    FK CONSTRAINT     �   ALTER TABLE ONLY public.test_usecontenttype
    ADD CONSTRAINT "test_usecontenttype_maNhanDang_id_fc0aa097_fk_django_co" FOREIGN KEY ("maNhanDang_id") REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 w   ALTER TABLE ONLY public.test_usecontenttype DROP CONSTRAINT "test_usecontenttype_maNhanDang_id_fc0aa097_fk_django_co";
       public          postgres    false    4525    378    209            �           2606    85223 N   thuyvan_songgiodongchay thuyvan_songgiodongc_tramKTTV_id_5bdc07d2_fk_thuyvan_t    FK CONSTRAINT     �   ALTER TABLE ONLY public.thuyvan_songgiodongchay
    ADD CONSTRAINT "thuyvan_songgiodongc_tramKTTV_id_5bdc07d2_fk_thuyvan_t" FOREIGN KEY ("tramKTTV_id") REFERENCES public.thuyvan_tramthuthapkttv(manhandang) DEFERRABLE INITIALLY DEFERRED;
 z   ALTER TABLE ONLY public.thuyvan_songgiodongchay DROP CONSTRAINT "thuyvan_songgiodongc_tramKTTV_id_5bdc07d2_fk_thuyvan_t";
       public          postgres    false    367    5162    373            �           2606    85216 G   thuyvan_thamsokttv thuyvan_thamsokttv_tramKTTV_id_dde17a98_fk_thuyvan_t    FK CONSTRAINT     �   ALTER TABLE ONLY public.thuyvan_thamsokttv
    ADD CONSTRAINT "thuyvan_thamsokttv_tramKTTV_id_dde17a98_fk_thuyvan_t" FOREIGN KEY ("tramKTTV_id") REFERENCES public.thuyvan_tramthuthapkttv(manhandang) DEFERRABLE INITIALLY DEFERRED;
 s   ALTER TABLE ONLY public.thuyvan_thamsokttv DROP CONSTRAINT "thuyvan_thamsokttv_tramKTTV_id_dde17a98_fk_thuyvan_t";
       public          postgres    false    371    367    5162            �           2606    85209 G   thuyvan_thamsonuoc thuyvan_thamsonuoc_tramKTTV_id_ca34ac26_fk_thuyvan_t    FK CONSTRAINT     �   ALTER TABLE ONLY public.thuyvan_thamsonuoc
    ADD CONSTRAINT "thuyvan_thamsonuoc_tramKTTV_id_ca34ac26_fk_thuyvan_t" FOREIGN KEY ("tramKTTV_id") REFERENCES public.thuyvan_tramthuthapkttv(manhandang) DEFERRABLE INITIALLY DEFERRED;
 s   ALTER TABLE ONLY public.thuyvan_thamsonuoc DROP CONSTRAINT "thuyvan_thamsonuoc_tramKTTV_id_ca34ac26_fk_thuyvan_t";
       public          postgres    false    5162    367    369            �   o   x���v
Q���W((M��L�K,-ɈO/�/-P��L�Q�K�M�Ts�	uV�04�QPOL���S״��$Y�!L�BJbI"yf�(-N-R�I-K�Q0$�#c�)� �\\ wN�      �   
   x���                x�ŝK�#Ŗ��|��]�Z��ʚ�� �D��١,��L��i\�jɰ`�涮f��b�N�	Qֈ�[�=�M&"3"��#3=sR��v�����o���O�=��x��?E���2��C�-����*��N�,z1�=��x5M��\�-+�Y�Aq����^����[����ы��^��(�͢e��ć6�o�7>o�׽���7��/�W�&q����W�#�l���z�a�n���A ���G���-�N���c(��T@Oqu )��).L)@�R�C�C���փzO�5�@�AE`�	�T&Q�� ����68(�:��`�8��\zEa\]�`�` (P�M	�/�}ꋟ������/�Ety��Gt��ZqQl��m!%8"��:�(M��L�*<8J!�8�3S#�R/�(�e9϶��&^n��|G�1&�>2.!��=�/!��=01!C�z��|-��E���L�A_������WJ�%@�%$P*�% �%�~� ګO�^���۵��7.H��3�^P#{-Eϱ��^@Kѷ�����h	L+�ٟ�
�h��fQ��*Kķ�*�(6���2=�>���Y���%M�4K��<�L���Vdvv�U�b'Fvjb%Avb`�v�-��N{�E���)��`�8(�Y\,+��	�EG![�=��O:jڂH�~x�I��W���=�t�KlC�x_�-��m�-俱H��u��hB�}����Z��X��%�;-`U�����oz+���4���p�5Iv�|��r�`���s �ST9����+�]��}7�>�v��B���A?_��Y<�p�O��{$�������9`�g������<�P�8��(y��ȧ��$B<�<�V���H-���H6ұK���4�(an@ �G���~#���}���h��W3��f.?b����GV��=��*;��ch��Dˍ<Fy����z�qMO���¸��K�|�-q�}Z,�hQl�����\��G9#W���#D�J�1i�G��>�L�3��W��q�H�쨷b�,[���yD�*b�mX�v�9��aQ(�3L|{�:9�)�7O�_�nn�/�B����]'�b�KD�@��Y`k�Pj%��;�TK���ݨ<��y!������_-<�шs���?ӭ�!�ǟ�34�1|�����XLǨ4�+�b�`3̣����������?�X�,�-�Tm�}�����)	���b<+�3��x(��;y9����}H���_��J���$�|�MQ  S_�Lެb2EE��I$ ����yLk�M�P~�FY��Jk�*��#X��}�qd�#�r
d�#
�r
`�#�R�����V��Q���N��e��ף<�S�+��J�E"�}����%LW+���5�E�؇�
�)������-P��'��N���7=��֑�ʦ�c�X�5=�iU�Q���p����#k���:ƙ���#	�N�m�D�ۿx!������X!{g��nb��ǘ	�Q�E��˅���fڠ�E��TB��^{g��ӭJz�P�݃��&=�?��u	�s�S�JJ����śa����:���>I,�w���X�:���q�V�n�r�^x��u�՛(�i���=��Z$s�)�H�����n�ғ��nR�H�I��7�K����:����N�^��R��6-+�iT���dhp�ܔ�3I8���O����k���۬��n��*o��V=���*�e����:_�(�]�eQ���H�l���+��x�Uw����o!���
<�g[A��ѵ�w�������<�$��|נ��8Kr���{�#�ҭirΐ���t+�����9)]�$g�zxvO���d��]!�(��+����Vh�VT*�IR
=ܯ�ۭY&���H�V1��l�v隉�������|[N��

y�6�[���!��&t˓�����|.��o��]t}������I}�-�X�y��zU���4y�_��G۸��2^�E���F���� ղ�{|���}��;e@�������pN�����:�~O���Et%��\�xJ]݊���U�x��&#�� ��B�$F^]{b kFb��ߞ�1'�鵽��rk�*��dap�>� ڣ%A�&��%��0�BKazO�62�Vn�S�K��if	��X��ݭ�l��i.?-3�ۼ3Mr7�w!"c�F>Sh�GVh�.uA6��
lzJ�gPh����&7�[����z���mE�o��.�y���k<=vX]W�U4���o���p�IC�''���N��399�	���|��iT豌fH��=��X}2��e���>����i!/�[�����^lTl��8��
{꽨>��ӆ�A^Z�^�i�Y!/�[��m���j~iB�V�~K^�h9�;T�Q.r�J�f�rඪl��.lH�)
���KO۶*��h�i�U6땞�������]C�#0N�l�j�U�Z%�N�\�8�R��]���S��o��kH�9�cNY��f�[ŉU��n�U\�T9��f�[A���F���dC�|���ԧqr֖U�m�L�ڪ��Y��]�	��Ć4�<3�+�O�L�'T�Q5}���f�3�7V6ʻ�?�do���FD��i)�T��+-es�a�,i	O�6�k�[)6����y'.�R1�:N�:�}�V��5t�>��
�z�M� 邌��Iݱ
1 s>��Y�JD��9��jD�f���ͱ�x(����HK�Jh���Q���-I��D���eh#��M���F�D�
޹J1�OV����^)�BO����	b�~���������ոJ�B���'oo��x�$���S?:bgk���,mw!7��`'�#qw�O�`���.��B���i�������A����ğ�U��۱
H�H�3}<��!bNԑS�aTC���c�`à�L91'�����T���[yd�zt�tZĩ��<ӏ��I��@�P,��T�6��2A�]��A�T���d���D�_�Pƈ$�����Ӻan�Q��",�m�Aj:`�֛kì��$Q���ӺG� �2j~`�`͏����͛a����%I��:Bľtt(���e�X��I��;��rnI�y�xw[�	I\�b�rD���[S:�~��s����ur��Bճ����T$��*V'"ȃ�?UX�n�}9Kcy��,�^�s	���Ӥ���؁�ɍo���؞��Ct2Tgx��F�ي��Ź���Y���c�T������bX�CA��yv�C��j}�-�(B��}McC���1M� ϼp���S�c�8p��ԩq.�R0�q��(�b��_o�d�c�Ƙ&��'Q�a�fhyz!�h Z��_4��P-<kU~w����k�Ȑ��|(�"�	��a^"��Br(�U�yj!9:nՃt<���}ު���#�8M�ώ�ٲ���ꂳ�E
7����B�2�3������U���Ij��i�:K���^�~���	'�!.�264dU�Д��Ѐ�+ƆeZ�o�e��r����l�ih�x4�HɊ�	��>&�'&`���J!���ۇ�_�hz������mg�Nj	kӸ��U'��1MON耩��F����J�l�����YJ��Ҵ��������\;�Ѣ��Zv_����h.��ү]��e���$����]��`ٹ��Е[˗��]�+1�3�wW5*t1�r�s��/uН; mb��Iڶ���P���^�c��*�f�kP�7ۊ�&��gtC���zp��kj������%]3��LL<:I�:{W�-SwE,?uNy����˝~%秪�ZI��_��iw����mA�
��i���U}����4�<>�$~Tƽ+st�PE�P����0n|�K}(oޥ��FIC��:_��mr5����4)<p�-�5"�=�"j�r 7�-`%J<ӣ|y�$-�u9f�oӨH�}r��/�t���vZ��XR��@����	ClJg\l8� DV
���Tv�GIu��͢������N��W �  ��r�S팪̣��2���l)=Qɝ�e�L���� O58}�b����O]I���k%C��Sס��k#��ab���P�qz-�H�<<q��*��ܯe ,��O�<S�,p������L�r�O�y6UO�<� �=�ZQ���Z8�����>�@����ۭl��z�\���r�s��� Op��6Vj$���D����H���	d��R�������,�e���]����N}� �0p���� �S���VC4!l��h:4��U�����%�J�$��n��c�q����<d@idxV���P�]��F�@IU+Z=�/H���5� 徴0Vߊ�{iaP׊�b��҂L�J��d��I�y���m�J+ۀI�D(I���]��<��i~����b�{9��=�#���j�rů�X�..H"�����%�1�����9ip��*�y>'������&��7�ؓ4�k��Ƴ��p���h���w�]�Խ�;�&p�D�q������i�WbM;q%xZ�J�'���6�� �Čؒ_���	[�}��db,<̃eɒN��@!�#��v��3�ߞ&�{�Ch�{z:�A�謙��t��
����d����a���v"���bǄ��P�S�$M��`�)0&2����r\*M�Du�V�U��f���7��G�.�Y�M��'4p< @e���N��Lmу�i �����W��mU�-+����i|;˧˲P{B����N��`����NV0� #�Se(P`n�o(K����(6�3=�	{�~�C���Q��F�1gz��� UЙX��ؖr����W���	M�7�[J� ؞� J� �t��4�!L+��8K�E*8�h�v�����P(�E���d[>%Mp��7�)1"��	P	���Mx����y!IY�~S�gv�h��vz�9��0n[��@����!6}�l<�U�zpq������j�_R�_�˻ڞ�̯���2�h��i�C�}3 ���>,�w�T��iU���^l���?>��2^ͳd��$Lh��)�K��8�����d`���b�dP����{U�脬z��j;U�Mh�v�s# �L�8�̿T�Nt�}��o�ä?�1�ސ�l����'���_d`$��Nu���镻=VU��yhB���ُ�爩��z,�#��M�ELfQ1�{T�j��ک��|��zg4�\���2����Ћ�LE�s�<�y1�QSL���I*���]�v��yZҐz�v3����3Ym�.&P|Fτ�]DF�=��H��Ѭ�tz<G�#�Y,Ԟ�J'	���Xj<�V�oR,@�K�M�P�<�����#��<�=�L�٬<��wFb]��`�=n�qA��s��a��-z&h���1H��C�Hl� �X�|P8�0Ȅ��Ĵ��Y��;���l!��zW$	q�p (��Y�6 (6�$ 3���eZ�f*L�U�?no#�-ꌘJŊhP�����eE�O6\d���E�P6\����Q6T�kPN��T��cH�C�}�BE��\.����ʣ�l��A
��&XUn�$ 2䕐D�����%�-=Z�����C۷t�̊e�C
���c�U��ېĚ��	: ��Hφ��lX}�l���O�Fυ��K��hΎ㶛4Ed��$$Z �H�z�aL���dV�z4g�@Cjb�C>C�I���6�32�#�\ko��]�hbȸ77�{(9�����]�|�S��>J6�cx�9�߭�]�lt�=z���\��W�GE���⦄�	/�]?�.��CC��M�����V���a�V��$^UG������k���q������� B���.�� F�GUxs��;��'���i�˸��F����01���-�7�f�BbZ������Ńh��z����<���mmK����C|��%#M�wݶƬ`a#EV|k��6R`ѷ�TǱ�Q���k��L����i�TC�����5h�ĸ���T�Ą�x����=D���x��)�Uts�}S����O뮺��r]��Do��� �n�%&�����t01�����i>��� \�_��3KJ��,� �
�ed1��e{5d)��V��������Z5�IMЧ���6^�����,qȡ����s!E���~��-O91uQlo�YAB�M��C�i(�~�(�G�@2�4�~7Q1wiR��׉���L������=q��H�11!�ͤ������&����x&^v�ɁqO-%�Ŧ,���8qO��
ˉ�ғ	�5E����Ă¢���UT[&�U�i�@4�Oܲ�cB�"�Te`!M�c���2���ȑ΁���G3A"��^s�yam�4AS��ڂ��/���� '�6���T���S��HE���L5�ؖ�>�R�Zk���e�����L:j�V�1)��=Ilv�{l[�z�J�jy-X=:%g�h�S�)��9i�҅?���QN�O3n��vF�h����q:�{T�D�o�m�S�L��ڧɶ�?��.�u����D�G�%8��t�Bg�N^:�K��W��莅��Wî��l�����ccN5�U�I�ad�$}T�9�c��7�V~��K����r�ձ���Z�����G��s(y�� ?�(}�� '��a�0=���/����A
e��m�鼜-8 �_�p����
��<�`x���Q�a`���r�F�vd���G�a�I�k$X��W�u��8��%�:���NGs��U��!�>�p�C������O�k�V���"~5.b�ů��Y��7�����RA}��:5)�(`#��PJ����J_=�Dѳ��ѻ/�{u̲ژfq�����ހ&���H[0ֳL91�5��mʉ	,��j�)'"�9����z�ߢbW�}?�B�m��d^�ಌ�h����ԏ��N`#�sg�d�628y��U��FeZ˯�Y�?W	$��i����M�A��ͣ.��`;zd'�h�s��i���bQ��ѓ��b�o��Z�ހ&���@��n��#����l��>���W],��6-d�7	��7���N'��#�AV����Q���N'M�#gq�wm�E�O�!M$wp:q�0���N����u�&L4���H�'-��/�qKDE�%�&Mt�`��t�#�~Ct����X�!�����wE���I}���B"���c {A�_=,T�msW�I*|�������ѼP:����� ٱ	�*S�뼙�P�B MW{3��q%���pϱ;�WE�^%y\y�4aG��S�Hq�X�JL#;����05I���i�>�3�}��4M�HBߥ�@&+���[j`�B�*6K ��'b������ҙ����p'�M�7k��ѻ�ۇQ�m�����eC�0�m�˨���Xo�������˨�mZ����h$?� �Wo�w{C���Ft)Q�1!;�Ť����SQ)>�����/�e4�^�j��6�")�˯L��A�VoD�+[��<��&F���g��xE~�q�(o��m��β���/{#�Pظn�S��I�D�!��5!t}=���KM��<�`��t�~kt��F�����IV��U�
��D"	]��6��s�Q��.������'_2��? >�K�d��0��&[r$�����θn9r���[愞�gʪU�1�����Eϒ      /   
   x���          0   
   x���          1   o  x��Q�n�0������ئ�<��Ҫ�^�!Qb	�HU��vR�?�[}ٝ���J�\o��-��t��G{����ն��5��ʮu�Ÿ&���Cc]s�T.l��ɏ�+��ctn�ho\�\mn����z�e�K���d��W���U.8\s+[����݆o�[c�����P�6漺��������?>����Y���#]���D��:U�`xI#��3�3�&�,���ē�DA3���]p�c�4�; ��fZϹH�"9K)� M8Oa4պ����^G2.RN�����DI�󲷕��8����h�_�!��șL	W�ґ�`]d,�IG�x���C:��c0�����ҁ��'L��tF�o�_�R      2   
   x���          3   
   x���          4   8  x�ՐMO�0����.�D����M9��
�FAl�:ei�F��`���=�@��#��o�ז�U�Y>mѪ�>��px��Zٓ�l%վ�u�Xu��U��h�I�JSIӄ�����	�i��G���MWV�ڴ�Ru�?��i�sm��������O�N���-;u{����>�����`M�Uesi�S�,ֻ�M�P˄��!�!
2>#�����d~�+�����]$<���O��	p���r:�<��P�#��(xĲH�"�4b�]~��dz3Z�w���E���~���D)e!X��`q��g�`�~9�sF�7A�"sG�/@�      5     x�E�Ao�0�������V&'�V�N��	�i�ȴQ�&Z���9�0_����)Y���`��`��t��sio�����m�Ms�wՑ~���5�q��AS��vi�2'435�����l�P���K�H���q�����:`�;k�'Z�����i��\�bbu�[S�����E]��"�A�ބ�}�cc8�����~�x�|BLAN0�硜s�1-��fC{�������1����e�%��H�AF�W�Y��0����	���V��KNL�F��/Ji�      6   �   x�EMM��0��W�T1.i��iQB��ի�iIvR��wR�y��r8Wp��	�����F2�����'Y�f-�Cb��1E$dq�^�#��`�_hZ�;7%�cC�C�p�������#�7�O����*�G���t���z��,��Լ��3��LI��r�T+����ت�B,�kY��(��'{���7I�7��N�      7   
   x���          ^   �   x�m�Q�0����$��֔��\e���):�~N{���s�ǹY^��eyyA��|i�������O-ջk�Aw�1]��G�R�� u�#�x�����ǧ[Z ��|���#�&Q��5���b�r�b
� Й�0��P���-��7
Ib���,����:�      8   
   x���          9   
   x���          :   
   x���          ;   
   x���          <   
   x���          =   
   x���          >   
   x���          ?   
   x���          _   
   x���          @   
   x���          A   �   x�E�AO�@����	�m���ROT�6Al,�J�a7�]4�ȿw�&�a�f�|/s(N��E�
�x�0궖V�U�*�l;|�?G�zM,:i��t�r�i�EZ�����IX�&�[�N������	��S����Δ#����x��:��KxO������+`L�+LV" L�!n��7d�<'��1��)�!0�1�l�eI����&��c�Ew�!Ya![�{��>V2      B   
   x���          C   
   x���          D   
   x���          E   
   x���          F   
   x���          G   
   x���          H   
   x���          I   
   x���          J   
   x���          K   
   x���          L   
   x���          M   
   x���          `   
   x���          N   
   x���          O   
   x���          P   
   x���          Q   
   x���          R   
   x���          S   
   x���          T   
   x���          U   
   x���          V   
   x���          W   
   x���          X   
   x���          Y   
   x���          Z   
   x���          [   
   x���          \   
   x���          ]   
   x���          a   
   x���          b   
   x���          c   
   x���          d   
   x���          e   
   x���          f   
   x���          g   
   x���          h   
   x���          i   
   x���          j   
   x���          k   
   x���          l   
   x���          m   
   x���          n   
   x���          q   
   x���          o   
   x���          .      x��]]oG�}�_Q�K�թ��>�ذ�h-ٛ�LP$-r"5�T��C,�0�`�� �h#��I6+b14�?�O�n5�lvۊ�j"A �ۖ�s�֭soݺu���;{�������p���Jڿo������^��a� ��k_E�֠�O��:WQ�����=x?��s|�����̓��յ?���Q���y`���O�t����q�}��sb�x�[߾{m�J��W(�t�5��!L$�*C�?`���>�y��W�-��Õf��i_i�?|��UTx��6�:��+{��1���4�W��+�/���+�.�@f����77bb������`�s]d�?�i�J��dD��uۧ���^�ݐt�4�"K	!�=�j�૖J��;����`�T�`�Q!953#�}o�:��P�Y�y�v�7}v��&�G��?�	xI�Cϗ�Ւ�hi��fhE-�	�����^o�dx�D$��(Y�!V8K�����6�X����V�PZ�C���ex5F��<7K�Ra�����k���`ƭcSİ�
~����h�7x�^}��?�8O���O���E���P4�H���ِnmG�I/r�c1B�A�:�
<��ۋPφ��~��V`�1b�-+�ebݰ��V:V���wDy���4���(_������=�������/�׊c:xpة4s#ڀ�hu����\����+���,q�:��(Y���b'���HoB������eB�:͒!h��xd�9l���EW"�e\e���~��/�f���yV56�k3���Dq-��FH��ތ�%Gqspo�}m����)�s�R�ҥ�dZ&��΢��|\V�넩!�vs����5S���0e��%��^0�>�e6`����Q��L�\'6bbx6|Ν8����V��ې�:�#d�B�J��/�����A�h�J`�%��L]��Ͼ�D?��dS!Dxw�a�XIQ� �j�ʩ?b��Ή�U��I��ڢ�iP���-H�D7�H��,�M)�jBy֊F�iW�<��X
.�a*,�z����OVN�3���DrC�%.�CK�~�g�s ���?�]��٦2�߾�#(�1�Vf ��H9�bc�oc�)��#�wk[.8Z2]b\����s+FI���L� ��X�}�Eݾ3��l�Ԩ5֋j�^	׹#q����t�v?�\A�§זZA�����X�j�c��������s�
ޮ=}hW�O���d�E=�b2���}��н��v��1�c�!�A��7	%���ǉ�������ٟ7�5`�h�A�*ʱ�ey���˃�i�8Q�E�V����8�4`��o���<l>;G���_�a���/�[�7FE�i	�����ZE��bf!�̙i�W4�@���a���a����{M��6z㿦�OOF�9������n� ��4�6>'?cz?'	U�H���e��H4�L��L��9rl|0췲���ي>��R�y�j�/�:�T�K)�
��X8��D��*� I�H�냂%�"fA��k[7�)�G�[��^g����B��gK��n��p$>6��ðx��)�ͭ{7�llw�:�� :B���R�0+��<�����6?��8F�$U�DiEp1�ټ�=�wk��ѓ&z�;�x<\��1�4H�I$�:��K����3؟� ʾy�sY�E��4���jn�*���1$*���n/�N:鴐�B���=[Kx�����k���ip߷KE�
�I�.b SAZ�98|)����h��7|R;�D�>ޠ�!p"�K^L0n�c6u*4���[�LF���p2��rj#���XХ��8� �	A�L�N�GmkUg����~~�*�;�_e�f��y+��38֭�4����sQKi�HuEb��e���&6ta���RmLhcjzAv2�1�ú�e&�(�;��
x1*�}x1J )�W�ہ?Aǝ������N�>�(I	�]P)�.ؘB��vr��v�c!��7��a6׬8�'�f�{�
��&�����"��M��@g�dB��A��ҥA��}t:h��#>rd�mLq������V��}2z�Di��a��-�A��ؐ�lPye�L%"8�i	ޥN�g�}%jG� �8�"�rC���Cn<���^�Gn�c5 �K�X���	�L��F��:���>:=n�:5[��02EB��R�q-�����h�b5;�p���؟��Q,H
��8!/��Aw(g�15�%�m��G���������W+�%�=������Z��]2o���6pb�@XD�Hd���vs����������p<1�0"u~�"�ρoF��Q/�T����UY�8����?WjE���@[!ǹ�B�(f]�z�Љ�X�U]�*?�b�lE1����LY�!_Q�e�'PŦ�5���cU�8^��ϡ��*6��KN��y�,�,�4L	�s8���Ui�j�F���"���J�G	���$d@	N��,?@\�}�]�Q-�$9mq�ld��F��=��g�F�|{�h�Q�1ei��58����1�*�"��7e�����R�S�����,j44�4!T�y*��9>|�C�a�C\�=ڕ���2,��[SVC�`�Hlx.��x3,�A�`Y9�B&Zi�e�
�kY8���P]�y;�,�w�2�Z�qO��ά�Ćs<��)��#/��<?x3w�q�)�(��V�rJȼ�K��}�����1�6��C�sZ���L�ǂ����N���|�jڻ���n����z��i*�\�|���J}��tCX� ��;�8��/����@ɗ���$)��#�t����q��C��-��AhNr�������L�J�S����/�h�|�}�g��pb��W��s^l�;��/$--z�i��Z����age���_-��'JS"}����@�_�ra�Ra�+������CFF�̷~尒ò�5��U6X�U��'�1P��6��O�R�Пl�����⻵��}?}��h�5=~�pܲ5�xt�����g�%�Fٳ��)m�|�1���2�Hh?�����Ԛ��-����%	�\h��(#����V�(9��82F��ޭ0Gj	GprQ���3�w+̑^��s�C�V�#��#)D�az��-�d�ȑZ泳&��w+�Yʑˤ �[a����ġ !Q��e{o��y#��;�5m��\��8�2�i�PMu~����M�T���Y�<#C(��<�#��:�N֤�q��N�}���S�v�ñ1���h�����J���:�\�<����������~gw�p�����aUc�8)XЗ�VW�ǈ6z9�1~N�j������h?˔�3q�C�p��M� ?��n���_W4���YDk�b׽�B��e�|��:��5\�Sd���~�.-ޤ{P�*Ɔ�d኎'�b��+����{�Qa�n7�j�zp�:�\�E^7����2)?����gQf>��"\��M~���^���A۸�T�WXA����Sв�4��J|
z��"�wz�h�N��hE�h��V�+ӆ�k�
h�ۮ�����#+}�ڵ4P��2`�Z������X�"н]��*<y��U9g	��]�����h��h�v��۸d��y�o���\���<����V��?Y�y:t�/��_����Z��9��~�i����_�YR��[+���e�6�d�e�=��[��J����٠�V%FIn=[���)���!��'�����LV&ڕ0���:=����w� �Z�����h2�c�H�ud ���䧔 SX�ʉ���d���Y˺�e���	�J��B�--?�����㺩Z�<� �C��w��G5N܆���a}@U+�(��k<�:9qc(3�p;��{i�v��w���!g�m�ew����ص~K�/�;�d(y�67h�����V��#5e_�1�N!���My�V�t}U�\�r��oJ//��,�c:Z\J�)͕Xq�����[;�����[�����Y��tw�_��z���}�\'HI$�~��p� �	  �~1LQ
	�?�����X�����,~w܊?�=��i���v��m��A���89���8H)2�,� �$�����3t8~2x
��+�@�CW��Ppٖ�d�s��Ud�#�5X��NX�:=���@f#^;�X�A�TB� v�aϭ�F���٨�V�N���Uڵq{�Ҕw����~j��|w|1�
��L��]H���/ 9�mT-,� v�c�>༏>�;�O���d�v�P����$�Ԕ����IJ��.+#}A�EbWJM��s�� c��o`��]���U �S	�$O>�N�����ݼ�Vu�_�)(�KA8�%�C�����#��{�����׾����M����϶`>�Av��!|pE� �������K=���瘨������qkvq��� R�����R�?�y��K��g�uM�ɀ��p)�j�f� �M�l������j;��\���q�}4�p�����5?6��ka�q�A@�8͡�*��{�gd�q�Ͼ�W�"x���(N�/��:=�`�4���z��d-�N�?�[��ǳM���p�C���#d���Ȼ�l/n�/��=wˑ�ƃ��fQ��yo�Q�HA`����٘��\|�%Q��]�@���B�&x �\l�1�fJM1��QP8z�y�fRĜ|�`�"��[�(�sD�N�'�Z�<_
G��М��]j-h�I��V���բ���h��V � ����5��)�����'Ck'�9'�����$8�y�+[��G�};]zH\�������x���v�S�I�	���J���);^�℮"�C@)�?����2����4pId+��?�mv�t�a�TZ�9����GN~�3Q;C�B�/&�j��{��a�sr��w@J��F��
GJ���W8�X�Ӟ��0��Y2�.�?��B�&z@'*w3�'
�s^~^[��nol����W�gF]����J�k�7��?+�ۛ#���G;�?���vVЉ���H1/o.8=��!���h�ޛ�v5%: u���
�CA�Y��Fzzl��	�.l�����m����ՒU�@/OF�W��F9L@ (��ʟ��y��w\|s=B.�����Op�|�bd}w�n6`��O60�[�g�Ë|^D�?>����;|s�^���՟���Є���8��E�p�]_�ٽ�w�ڝ�1Qփ�	������ˣLF!r�`���֮��\��z�5<�]Y�)�BǄ�k8�&���O�z�Ĳ8��]Og�0�r'��C�z����:��E:�e��*`���5`��^8؆m� M.�Vu�O��]V�.(�"1�Nz����|	,�F�wn��w�V�ƾ,|�����i�c��U~�'�p����r��>�|�s!R&�*�2ᮾ�*�+/mL��O@
�weÆ-���s��IƊ�~~�������\ �qB���=����f�ts�:���Y����vm��"ejHC@
�oPa8%Ƴ�pr�?�B� �*��%Xz��MM&��dT���)���5�c' �]�mhL�e�-Yw*������@�:T5o�3�����;��݀샻�m���G7[kۋ���s�v2����"^ؐ�m@�Ɇ��(��wvJh/[���m�R�t�H/фh����ik�;hG�.Z�6=�n����W{8��{8����
+���.��\�Ѹ����ݹ٭ٖ%1g�Y��:p"\��y��w��F�f�e�����,ۼ� Q��&%�R#�
�T �-
G�	��d�C^����Z��S�+8˄��Ӂ�2©��p��д���t�����A�n}�(�eq���e�y�Z�L7%���<��Dv�h?�����`��j��W��]ƌ��?P"L�s����0��\j���r��WLs��y���`��}�Hx�*(̷uIr���v�`S_����R�2��_�P��G�Y���y+;׺qo��^V���u�@�/]���J+���P΅���'4>p��w�`uK�S��۟HI�	L�y�b��Oެ��A^�9lg{���#t�&�_A)����lQ�~��s�H�_����t����'�pN ���԰����o@�)_E1��U�%���KG��Ϙ�օ�je��Ȯ.�~&Pm��r�,��}���4K�_܂@�n����p�..�~</��o[��4��yZ˃]Ի/CB�if�+Fx�V��g�;=B���B'|�x�sܻ:�A�,�B��W�8� ܮ��6-���1#}_�Q�J�5�lK�z��Ҡ]��M�!ܩ����҃���H��%�nƜ���D7+ɛ�
���
V�������'2�b$ W�_cZZ���L�P�($�V��-jPv�5	1��G'ٝGռew�����$��͕!7�����~��e���         �  x���ͮ�6��y
�n��[BW]d�H���6�I�b-��E��wH��M)Y����Lrxf8}���ßm>~��M7j-~����h��Z��/�ک�[-�ox�}��A��7���~�������y�߼p����.js�/�~}��|�l�Z�Թ�}�M�k?�vo�w�_��8PF���z�]� 95��ŵͭ=��`�?�h]�Cs�� l}�h�r1��ǳ:\�%5{Ъ=j����ő貫x��D��ʞU�>���ϓ%�5�f��i�gB�7��|�_��&���i$� ���|�8jde1�ш�py��g�H����(K�x��[1�T�H2EVB���
�0�~��kŤ��|Q_^��U�= ��F�N��x�s��	�-dɯ�k�%�	�IHD�=�T��'��A�_�]'���3� ��߷��0ه	�����4��A i��S���; �X��Jي� )inM5n݊�4�t�D��Dr�q�m���A\�i� �6�WQQd]qD��+2�O��7=o�ܶ�y���iDeh��ӕl��SŁ+?��T�ӈ����a������/@�DZ�5�������_.�z~ �.��� c�<t��%��\O�.��'�~�[��d�2w5���h��q�8��X�B�P6#8k;�<�<+��<*=Pg�G�fMw�O��%N��n��^i1�sy]��U4FSW��=��`�&e��<�ӌ�4��F^$_��\֖U��&q�G?���%�I�������A+Ħ"wl
����wIؾKt
("�!z�vY�pqpӂ�G>�vf7�T�D�FK�8�r�SNm\ ��SHí�>-[A��`�7�]�47��ш�t��gW��nj�~HtG!@`�S@'x��|��}�,��@DzSk5T'	��{�!~��7��@��(��Cgo���	T.�\;�t8�P�{D�g�7$�=V<�T+�CY��[���T�b;á���8��ho۠{����{B��H�`Pd!�Ls!͸%��8�]�\œr<��5l�I=^�����$6�,���cǯ�"]5A�N�h�'��lc �Yb���W�jd,P&C�*'���i�p���Y@�g�_�á� E�]\8>Z*wc�.��m̜ԁC��杻�;�h��`#벘�^7�� ����H���B�v�4�Cc�3:$
hȳ*�Mf0�S�4�Si��]A��g��8`Fc����jp���~�`^ w��7�b����3<��m���8eg,���0xȄ;5�[��w'k/HR �hz��`y��I �ߺI/�Bf꙯�o�1�IU���9�ԇ��vW�i�倬m��Q�n��	�`\��bq��Gn`Vgu�v����)��K8M�>$/[��!E��9����k��'������i	��[2�8w���&@U.���'K��2m���FI��g`�������KCL'w��ĤO���s�'|��'D�,��"K�U�S�8X���ʂ*ڿ������E�(~t'iH\�	�Q�u�����kHC�?��g,�I�?��]�=Sc5gtUqߐw,�1d�'w�[ie���c8'I�k_р��b0�eDW��^j��s|m��h�R�9����Ыۗ�w�_zy�4�5��f�������(6�97pe�Ȓ\�ǵg\�ڛ7�t�GV         �  x���Mo�F����%Abgvg?�S9(R�i{%h�YK�"QF��;�ȍ��.	 ��Hff�yg���|�����_��ms���m���l�]ql��o���y��>l���æ-��ӗ��ڽ���˯~��y6o�]�Wm�?���[~����i��)�5*ď*|�Q>ǐk�������{���7�EPp�su�����"����b� A�M�G�׾^�D���߻~��mn��8�&Ȇ�b8vǦ]��yQ;b�����>Ώ��R�S$AyΌ��)�P��G�5U�o�fה�e�1؀$
���u�r������)��ue������
�)��v�zP�'�e1��V��2�it|fe�����/a+�h J��z�cřYF�2eX8dO
�	塯�E[w��_˶.[��}���v�N���i1(�Y����{��wձ엦PkMV�|G�T�K���UNVT�K�Π.������B����W�a���}}}|(����:Y�f.�k���9�P�`�C�#f����ń��\�^kY/�#k�=���]Oũ:���j�+�3��N]��r�� CvKǒ�^K8V4���A��8v�c�8!��=�N�Y3+�:-,��ark*�;�#me�?�D�&5E
R\V�si5�_�c�t��H��S8\HZ�J딈O��+\>�0�9�6s������&iKp)�Q2�,Y�񾺼jo!Gʬ�JxB�vȀqu�bVl��Vc"�+�GŁr�]W��"��2#(�\�����@xr�~ʾ�8b���L��"��d�sPn�t�tN.z'g�~/��Pǁ]�
D�i0G���v	�tc��~��G�瀙B�0WJ��-���}h�m��4��:W>�܅�'(3+�a*0Z����s�2�9��ue�������4 �b�!Η�N���ό�{��L,��E1O%��=X���D	�'����[_[��C5�����x�v�&��A��a$����������a��v�������h�t�Br�������'E��q�۟�6���]���n$�v��1�<� t>��r�J�d[p�qL�-s0h�TYA�$3S23C�}������_3o'pR�h��@Q�_^T,�ѐ�hXa�EO�����"o�8��,g��g���$�F���l]���H����$����F`�r`{e3�m0�5wK9�$��psY&;��\�ú�3E��V��^]�����9�32��I�7��!��B�V������ �##|�`))vL6�'x�'�2�N������ء��d5pQ�2��,��p� �2����"do)�����9�
,R$��pjF��Dʒr�#���-�h�{*�`�l�N%sy�0�O�+N'���|�� �Pn��kb��'�������eӟ�}�b_7��:�sq�i\�Uf<��K�b`�GW�&5�"qD%��s�]��E��=�Ⱦn�����/�~�\.'?��:�O0ͺ�W[4��$��8S�y���J	����9X��۱Ө�)`�8�2��U4��-�x���ˑ��'V��&	���8��Q6�>�q?Ų3X67\g����:���ϥl��~ocCJd�5�ŀ({J}��T��b�eֳ=��D{@�������&�޽���Dm�,�­�'��&!
ްņ'�3�>A:�<�y�/�6�      �   K  x�5��n�@ @ѽ_1;5�k`�+ATĀ���!#3X���vw�����>0,�u{���<��2��7�J0���_3��4~�3�����x
��}�{`2�(a�Hd!��آ1Am2����2i5�����c��v�/G�#,N�V����E]��G�|�~�$�"�,��TB`�(�`�ۤ괷����Y�����c�<����{�C+���^�!2}J���{EB�j��(�g��_*�H��|P�lX���lw�	>��A����C[����J�hŶ;�d�sC�s���k]�����gy��X�E�C
'*�4G����+������
�{         �  x���j�@��>��E-��m�'��!��Ћ�1����qڷ�+���ko^z�/�t��'�R�BO^����	��t�FA�E70���bD#q'0�	��h�B��A�B>;�.��.e�Y1�ZU��E�%��#⯩i|-#S�a�M0�)ϊ�i�; �*$"t��m�(ʆ��DlVwi_գ��h�P��>�_��W͕}/0�J0<�0��-@����9�FV�R���Z9W�\��W|1{y ��tM�T+$t1{e����F�N�95_�4���f��$B�/~jZ���U�y��'Dc�,f�0$�7
��~@c��'��	� �5�D��t����l�'x%�Q4w)V�h�~��)V�S�k�%�
�9c��0�?��Z[�D�H���CY^l�uU�d��|u���            x���v
Q���W((M��L�K)��L--,M�+)ʌON,H��+�T�P�M��H�sI�KW�QP*I�sN, ��=�AtzF�sF���B��O�k�����K��������������OjYj��	ƚ�\\\ ϖ%.      &     x���v
Q���W((M��L�K)��L--,M�+)ʌO��+�T�P�M��H�sI�KW�QP*I�s����22S�<�Z�")����pnqJI`0�������%g�&���M�+ER��QZRT�����A22=#�9��:� ,�����'f"�C@LM�0G�P�`u�0O#sK##Cu��̇��K�L�?� O���(���Ci 4�Mk.��p�4� ���p6��y�{=�oa6��vcl�>�Tgl�l8��i�؂݈6��� I�@          ~   x���v
Q���W((M��L�K)��L--,M�+)ʌ��O�L��+�T�P�M��H�sI�KW�QP*I��J���e������J�
a�>���
�>.a�F��FF��:
��E��`���5 >�%�      !   �  x�͖1O1��|��,	��QP��"5j�V�@l�r���	��`�:t@�`d@E !ڦK�C�|�>*�y,��;K�ݻ������V?GP�E���-��7T�7ծ�����N�e7i�o3.c3�v\c�x����eSTqQ�������0��������5�)T�rX*.�a1(�Aa�	ɸ=��ܴ0�&Wy>�%��?0sҜs2���~Hn.H�]�����0�`��]_�����h��H!Q�b�aJ׭�1��)Δ� ǒ�=s���K�.Ma�;d���'8oY�3�/��|QH��WAƼ4Ō����-������q.O�Q�=ӗT(A��=p@E���G�1O��·��2��	R���"�\�P��_	u��@f�h��J�Q���=B;pR�%R2������z@��# ���t��u��z�f7m�k}
T.�f��F�}�Q��ލ?�������%���$�P      (      x�ݓ]o�0���V�D�Rp��@�]P��2�|���`'�$N�c����¤���n7K�^�s�c?���������w��U��5�bF�Na��H��(�{F� �RRQ��<�ӈ�*`2�*�BI*��r��*�(�.���"i�Y|ٕ�0�Px��}�#8��[�8-z`�!�F�w$�30r� fmo���^�l�%!
���YF&,FY��wWs�wD׋�eJ�Ƌ���e���IB���-��
Fd�t��;���$��0�f�k�
������,.V��@��x�y��B�kD�	�������6��u-=������k�!����4��w�Ã�Y����[���8/�Hg��d��<Z8���FJ�S����s�$�g����n���
:�o|��olК 6m�a�������:���z���''�mE��G��G�3��m.��з�">v�eWּ}Ԃ�a��Jr�Gb��έ�&:V�e�f'^�l���ek�ޟ_%RT��AHښf��o��T��8o      *   ]   x���v
Q���W((M��L�K)��L--,M�+)ʌ�K/��L)�K�O/�/-(V��L�Q@��x` KS!��'�5XA�BG�HG��@Ӛ�� � �      ,   {   x���v
Q���W((M��L�K)��L--,M�+)ʌ�K/��L)�K�/-N-�/H-��,.���+V��L�Q@ȃxi WS!��'�5XA�PG�HG���LӚ˓.6�m422����P?Zm�� �v�      %   �   x���v
Q���W((M��L�K)��L--,M�+)ʌ����-I����O�S��L�QP��IT�����@VzQ~iA<H�(?'US!��'�5XA�TGA]��XӚ˓���!�g��`Dk�̑�3�Q0��}����l��\\ [��|      �   0  x��Qo�V���)���V�l �=IIYpX���[�%v�쭊�>L�U{��jeQe]�v�4kڃ�|��{� !v��/	�G���s���s�[--�I�[��C˨�5�qըk5�!����U��W�����<�ߐWU�,�d�~��5RT��V#���$eM҈J/����|
׷2M��ȍ�L6Y�W-�SVneUYw?[�{e՚�y�U�u�)kR]F˫�$k�u[��[��[o���Ӆ��<|P�K!I	B$� 6�:��"{�����O����m�!��@�73��,����R�F���Xw/}s/7gl�@�:U<h���یm4>���}Ƴ摭Hd.;hX�=Bq(� ,�c}�s���Y�� �
a�=����m�]AZg�
���l��aw�uر>�m+��Q���b�lqj�e��xm��W��G��x��sPl�� �iw�8�@']?&[&0X���g�!֡b�?q�A"�F(����T��#r�6��<��(��H�1X�H�V\o�R撫�e]��0@���{�R\,ݝ���x4���H�<�FsQ_��g��U���V@�D"�v�����W�B�O���~�X\)�d8���'�G��v�z	�u�[g��-\x�m���)��k�g~j�޹̪����zw��Μt��S�n�@�إ�q��F/P��m��KDEa9S���b�)���T��������K�Vy��t�%���ӄ�&}�Ѯ�Ncr��`3&�����x���F��\�O�I�)K��S�e��zϧџϵ	��	ȇ<D� g��� �%n��e��r�p3���a����'{P�tC���4�l�;2���e�n�M)�
>���d��N��~�ـ�� t�i} �8�@�'�1�-z9���ě`uZ��{K5��߹R=3tO�j��W�ϐ�$8᫄E�'3���c�܇9a/��0a���o��!��,��3y����@o�)VY�^|��
?斣FfH��D� JB��F�B����SJ�S-��-���&����(���'�pз ���cDi��B9��$9gg�{�Nφ�`K��9�@)'��MwK���y�C��f�{���v�
9�ک��sd�US�f���'�H�}v�H�EL'��G�P��W=�v�ߣ!ҥ���ߙK�.e�B��,Ʋ�2G(j�Z��2z����RNZZZ����r�<�g�x�>��b��"؀[ZQ��L]yN~*y�hi3
��L�Z�Ϯɧy����YG����рlfm���[���"��ݓ��	��ԭ����J^�:"�8�@���Lڭ�Yq��4+�>��{�']�lnM�>hT�E�2d�%XHq�Cw���[Be�S��N�:��Q���$�����X���R��"P[��B�q?dyc�K�1��;�,o�x��	�Ť�+6�Ƃ�8�8xqP��Yp�yMp��D�qo}j��伧�:f9T��m���?+�ó����I���>�L"ק�d�~��W� 2�1j��m�/�Ea�s�ʝ���S���Lݜ��ujj)��|y%��71�_Wb���a?њ���I���tc�5��0-��2B.x���9~tO�� �˭�p��[��tF�)���#LCV�aя��:��:��c��!��6�}=���Ba����\l�-�6�A����Wm�D����7ñD
���8���	π�Sd�<>:"�o�����,ᙷ������j��M�v�����d�͕2y�5������!���{z<��J�=�/�1��M8J�r��eo�����I��J�K� ��	a�� �w�}��       "   �   x���v
Q���W((M��L�K)��L--,M�+)ʌ/���()J�KI�
J��~�y.@����RIj^PMH:�	$����Q����������dda`idd`�����txM^�BIƱw��K	�kZsqq ֫/      #   �   x���v
Q���W((M��L�K)��L--,M�+)ʌ�(M,�(U�P�M��H�sI�KW�QP*I͋ �D��8����J�
a�>���
��F�FF��:
�~� J]Ӛ˓��l
�|���D�/1�n��=��p��������f�MG&<ܽ2f' r�k      s   N  x�͒Mn�0���bv5�l'�����H(�
tb�R��8�{��]wI/қ4�R9�y��}�i2�<.`�,�nW�Z�R����V��0T��0�j�B)�nm�v낖ϭ���e�֪6�*;��:��ҙ�.U�6ʦ�Z
cY�E��U[�*���l9�Ð���7N�݉<�Wz�܈��^O����kD����c ��Gԏ0�cr��s���c����U����(ݷUy����Jy�[i��^���}~�[�G��8!a��0ƸO�,��8��Dt6��(wp_߬3�y�J���A ��C�Ǆ�0�8P2J.@?�H�$      u   q   x���v
Q���W((M��L�KM,�O,))�L*-I�O�+�,��O.Q��L�Q@H�x��y%@%� ��B��O�k�����ZjZsy��c 22���:
@d��� �
a      {   
   x���          }   
   x���          w   
   x���          y     x��;o�0�w~��HT�.�:uȀ���$]�rE�"6mU���<EQ+e��;��ז��h�{:@�M��t�4q���В3��P�Vd5M8�p�rvb-u�⴪���K3b.�#��*�`儜~L�z�J^hIk�ŃU�p^�Tp:�R�;��=,����,����n+S��D��0T�c�
AB6��t}}4t��$w��<4�7}&���{���{*��ܳ�W��M�Z����=��|��#��by�Ep��!,2���8��*�	      ~   
   x���             
   x���          �   
   x���          �   
   x���          �   
   x���          �   
   x���          �   
   x���          �   
   x���          �   
   x���          �   
   x���          �   
   x���          �   
   x���          �   
   x���          �   
   x���          �     x����k�0�E�ĩ-�ѓ#ka���k���c4)쿟vcBw�e�m���}�ç���s�ʺ� ����򽓊3	-�䞁����I��,TPw�	hF(t\_��`�uS�^�Į�\w$6M��i`L����46zcI�J��>�v��� e���C�%)��T ��N9��C��UU��П�g�I����1����3ɕ0���*$��*(3L���P�\��x<�_�Y���]|���ey�����ߢ^G      �   y   x���v
Q���W((M��L��-�)��MM�L���O�,.��IU�P�M��H�sI�KW�QP*I��J�$A��L�R%M�0G�P�`u���HWCK##Cuu�I ���5 (�%e      �     x�ݔ�j�@��>��E)Z���T����R�^e��f�&�1�<�z襾A{�R���/�7�l���^��ο��G&�^�}�A���Bd���'��9�d��@r�bHz��Q~�
E�Ս����#'l��z��ǙD���d����+a'\�x�#�g�N.�f[G%t��$Äj���L"�J/��>�KL�iF��j�KR�Bi�!��k�ƕ.�(�l��R�<�`̱�o[��)
T�uf�'�F���_�}����Q�������D"|/wQ!�01WC���J��"�.�
��S	�b5�`�շ�����k��|�%�q���J�
�}t3�{9�_���&&!Cp�L���oD���Ð!K0����派;�g�P�3�      �   
   x���          �   �   x���v
Q���W((M��L��-�)��MM�L�����M)��L-U�P�M��H�sI�KW�QP����sA��<0SS!��'�5XAC=)35/=3?h
�R�QPa��ë��3�pd���݉P���5�'���_������s��
�w�:!�]�A�sq 1�^�      �   
   x���          �   
   x���          �   
   x���          �   
   x���          �   
   x���          �   
   x���          �   
   x���          �   
   x���          �   
   x���          �   
   x���          �   
   x���          �   �   x���v
Q���W((M��L�+�O�+�H��N��OLΈ�+K�P�P�M��H�sI�KW�QP*I��s� 1s�C��@��̌�J�x^zb��2�;���L-�5�}B]�4�A|CKK##Cuu��̇��s��^� a�ë4�)��������HcMk... O�@      �   
   x���          �   
   x���          �   
   x���          �   
   x���          �   
   x���          �   
   x���          �   
   x���          �   
   x���          �   
   x���          �   
   x���          �   
   x���          �   �   x���v
Q���W((M��L�+I-.�ϭ��OI�Q��L�Q�ILJ��QH���LN��L�Ts�	uV�P74S�QPO��OI�L2--5��<)5�dhv6��31��\��X���T��SV0���SQM饖��&�3ۈ��6��a���642���� ��ׂ      �   �   x���v
Q���W((M��L�+I-.�/-NM��+I�+)�,HU�P�M��H�sI�K��LQ�Q�ILJ��QH���LN�Ts�	uV�0��QPO9�(O!��u � ?3�$hVzIQf^Fzfb~Ji���5�'����ZW�Q�p�v��#�y ۋK���S�3SSJ�n)�[�� o�V@      �   
   x���          �   
   x���          �   
   x���          �   
   x���          �   
   x���          �   
   x���          �   
   x���          �   
   x���          �   
   x���          �   
   x���          �   
   x���          �   
   x���          �   
   x���          �   
   x���          �   
   x���          �   
   x���          �   
   x���          �   
   x���          �   
   x���          �   
   x���          �   
   x���         