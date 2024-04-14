<script>
	import Social from '../atoms/Social.svelte';
	import { user } from '../../util/discord';
</script>

<div class="socials-container">
	<Social icon="github" tip="rosset-nocpes" link="https://github.com/rosset-nocpes" />
	<Social icon="discord" tip={user.username} link={`https://discord.com/users/${user.id}`} />
	<Social icon="email" tip="coderpy4@proton.me" link="mailto:coderpy4@proton.me" />
	<!--<Social icon="kofi" tip="" link="" />--> <!-- TODO Replace -->
</div>

<style>
	.socials-container {
		display: flex;
		gap: 0.75rem;
	}
</style>
