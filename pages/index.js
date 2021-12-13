import Head from "next/head";
import Image from "next/image";
import styles from "../styles/Home.module.css";

export default function Home() {
  return (
    <div className={styles.container}>
      <Head>
        <title>CoderPY4's Projects | Maintenance</title>
        <meta name="description" content="Maintenance" />
        <link rel="icon" href="https://cdn-icons.flaticon.com/png/512/5305/premium/5305390.png?token=exp=1639422002~hmac=dfc628845749712553eb322609b83284o" />
      </Head>

      <main className={styles.main}>
        <h1 className={styles.title}>
          Offline for <a href="https://nextjs.org">maintenance!</a>
        </h1>

        <p className={styles.description}>
          This app is undergoing maintenance right now.
          <br />
          Please check back later.
        </p>
      </main>

      <footer className={styles.footer}>
        <a
          href="https://github.com/CoderPY4"
          target="_blank"
          rel="noopener noreferrer"
        >
          Made with ❤️ by CoderPY4
        </a>
      </footer>
    </div>
  );
}
